from datetime import datetime

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from src.scanner.vuln_scan import run_nmap_scan


class ScanWorker(QThread):
    """Run Nmap away from the GUI thread."""

    result_ready = pyqtSignal(str)
    failed = pyqtSignal(str)

    def __init__(self, target, parent=None):
        super().__init__(parent)
        self.target = target

    def run(self):
        try:
            self.result_ready.emit(run_nmap_scan(self.target))
        except Exception as exc:
            self.failed.emit(str(exc))


class ScannerTab(QWidget):
    scan_completed = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.worker = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.target_input = QLineEdit(self)
        self.target_input.setPlaceholderText("Enter target IP or domain")
        self.target_input.returnPressed.connect(self.start_scan)
        layout.addWidget(self.target_input)

        self.scan_button = QPushButton("Start Scan", self)
        self.scan_button.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_button)

        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)

        self.results_output = QTextEdit(self)
        self.results_output.setReadOnly(True)
        self.results_output.setPlaceholderText("Scan results will appear here.")
        layout.addWidget(self.results_output)

    def start_scan(self):
        target = self.target_input.text().strip()
        if not target:
            self.status_label.setText("Enter a target host or IP address.")
            self.target_input.setFocus()
            return

        self.results_output.clear()
        self.results_output.setPlainText(f"Scanning {target}…")
        self.status_label.setText("Scan in progress")
        self.scan_button.setEnabled(False)
        self.target_input.setEnabled(False)

        self.worker = ScanWorker(target, self)
        self.worker.result_ready.connect(self._show_results)
        self.worker.failed.connect(self._show_error)
        self.worker.result_ready.connect(self._finish_scan)
        self.worker.failed.connect(self._finish_scan)
        self.worker.start()

    def _show_results(self, results):
        output = results or "Nmap completed without returning output."
        self.results_output.setPlainText(output)
        self.status_label.setText("Scan complete")
        self.scan_completed.emit({
            "kind": "Basic network scan",
            "target": self.target_input.text().strip(),
            "completed_at": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"),
            "status": "Complete",
            "output": output,
        })

    def _show_error(self, message):
        self.results_output.setPlainText(f"Scan failed: {message}")
        self.status_label.setText("Scan failed")
        self.scan_completed.emit({
            "kind": "Basic network scan",
            "target": self.target_input.text().strip(),
            "completed_at": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"),
            "status": "Failed",
            "output": message,
        })

    def _finish_scan(self, _result):
        self.scan_button.setEnabled(True)
        self.target_input.setEnabled(True)
        self.target_input.setFocus()
        self.worker = None
