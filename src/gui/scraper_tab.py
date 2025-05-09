import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from src.input_handler import validate_url
from src.scraper.site_scraper import r1

class ScraperTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter target URL")
        self.layout.addWidget(self.url_input)

        self.scrape_button = QPushButton("Scrape Site", self)
        self.scrape_button.clicked.connect(self.scrape_site)
        self.layout.addWidget(self.scrape_button)

        self.result_label = QLabel(self)
        self.layout.addWidget(self.result_label)

    def scrape_site(self):
        url = self.url_input.text().strip()
        try:
            validated_url = validate_url(url)
            scraped_data = r1(validated_url)
            self.result_label.setText(f"Scraped Data: {scraped_data}")
            
            # Generate a report
            report_path = os.path.join(os.path.dirname(__file__), "scraper_report.txt")
            with open(report_path, "w") as report_file:
                report_file.write(f"URL: {validated_url}\n")
                report_file.write(f"Scraped Data:\n{scraped_data}\n")
            
            self.result_label.setText(f"Scraped Data: {scraped_data}\nReport saved to {report_path}")
        except Exception as e:
            self.result_label.setText(f"Error: {e}")