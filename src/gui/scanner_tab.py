import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from src.scanner.vuln_scan import run_nmap_scan
from rich.console import Console

class ScannerTab(QWidget):
    def __init__(self):
        super().__init__()
        self.console = Console()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.target_input = QLineEdit(self)
        self.target_input.setPlaceholderText("Enter target IP or domain")
        layout.addWidget(self.target_input)

        self.scan_button = QPushButton("Start Scan", self)
        self.scan_button.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_button)

        self.results_output = QTextEdit(self)
        self.results_output.setReadOnly(True)
        layout.addWidget(self.results_output)

        self.setLayout(layout)

    def start_scan(self):
        target = self.target_input.text().strip()
        if target:
            self.results_output.append(f"Running vulnerability scan on {target}...")
            try:
                results = run_nmap_scan(target)
                self.results_output.append(f"Scan Results:\n{results}")
            except Exception as e:
                self.results_output.append(f"Error: {e}")
        else:
            self.results_output.append("Please enter a valid target.")