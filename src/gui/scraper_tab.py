from datetime import datetime

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

from src.input_handler import validate_url
from src.scraper.site_scraper import r1


class ScraperTab(QWidget):
    scrape_completed = pyqtSignal(dict)
    view_report_requested = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter target URL, for example https://example.com")
        self.url_input.returnPressed.connect(self.scrape_site)
        layout.addWidget(self.url_input)

        self.scrape_button = QPushButton("Scrape Site", self)
        self.scrape_button.clicked.connect(self.scrape_site)
        layout.addWidget(self.scrape_button)

        self.result_label = QLabel("Enter a website address to inspect its page content.")
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)

        self.view_report_button = QPushButton("View Results in Report Tab", self)
        self.view_report_button.setEnabled(False)
        self.view_report_button.clicked.connect(self.view_report_requested.emit)
        layout.addWidget(self.view_report_button)

    def scrape_site(self):
        url = self.url_input.text().strip()
        if not validate_url(url):
            self.result_label.setText("Enter a valid URL including http:// or https://.")
            self.view_report_button.setEnabled(False)
            return

        self.scrape_button.setEnabled(False)
        self.result_label.setText(f"Loading {url}…")
        try:
            scraped_data = r1(url)
            self.scrape_completed.emit({
                "kind": "Website scrape",
                "target": url,
                "completed_at": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"),
                "status": "Complete",
                "data": scraped_data,
            })
            self.result_label.setText(
                f"Results are ready to review in the Report tab. Page title: {scraped_data['title']}"
            )
            self.view_report_button.setEnabled(True)
        except Exception as exc:
            self.result_label.setText(f"Could not retrieve the website: {exc}")
            self.view_report_button.setEnabled(False)
        finally:
            self.scrape_button.setEnabled(True)

