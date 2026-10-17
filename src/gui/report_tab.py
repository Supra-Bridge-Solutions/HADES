from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget


class ReportTab(QWidget):
    def __init__(self):
        super().__init__()
        self.latest_result = None
        layout = QVBoxLayout(self)

        self.title_label = QLabel("Results and Reports")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        self.report_text_edit = QTextEdit()
        self.report_text_edit.setReadOnly(True)
        self.report_text_edit.setPlaceholderText(
            "Run a scan or scrape a website, then choose Generate Report or View Results in Report Tab."
        )
        layout.addWidget(self.report_text_edit)

        self.generate_report_button = QPushButton("Generate Report")
        self.generate_report_button.clicked.connect(self.generate_report)
        layout.addWidget(self.generate_report_button)

    def set_result(self, result):
        self.latest_result = result
        self.report_text_edit.setPlainText(
            f"{result['kind']} results are ready. Choose Generate Report to view them here."
        )

    def generate_report(self):
        if not self.latest_result:
            self.report_text_edit.setPlainText(
                "No results yet. Run a basic scan or scrape a website first."
            )
            return

        result = self.latest_result
        lines = [
            f"HADES {result['kind'].upper()} REPORT",
            "=" * (len(result["kind"]) + 20),
            "",
            f"Target: {result['target']}",
            f"Completed: {result['completed_at']}",
            f"Status: {result['status']}",
            "",
        ]

        if result["kind"] == "Basic network scan":
            lines.extend(["SCAN OUTPUT", "-----------", result["output"]])
        else:
            data = result["data"]
            lines.extend([
                "PAGE TITLE",
                "----------",
                data["title"],
                "",
                f"HEADINGS ({len(data['headers'])})",
                "---------",
                *(data["headers"] or ["No headings found."]),
                "",
                f"LINKS ({len(data['links'])})",
                "-----",
                *(data["links"] or ["No links found."]),
                "",
                f"PARAGRAPHS ({len(data['paragraphs'])})",
                "----------",
                *(data["paragraphs"] or ["No paragraphs found."]),
            ])

        self.report_text_edit.setPlainText("\n".join(lines))
