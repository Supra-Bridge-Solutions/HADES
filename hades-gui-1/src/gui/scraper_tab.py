from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from src.input_handler import validate_url
from src.scraper.site_scraper import scrape_site
from rich.console import Console

class ScraperTab(QWidget):
    def __init__(self):
        super().__init__()
        self.console = Console()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter target URL")
        layout.addWidget(self.url_input)

        self.scrape_button = QPushButton("Scrape", self)
        self.scrape_button.clicked.connect(self.run_scraper)
        layout.addWidget(self.scrape_button)

        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def run_scraper(self):
        url = self.url_input.text().strip()
        try:
            validated_url = validate_url(url)
            self.console.print(f"[green]Scraping {validated_url}...[/green]")
            scraped_data = scrape_site(validated_url)
            self.result_display.setPlainText(f"[green]Scraped Data:\n{scraped_data}[/green]")
        except Exception as e:
            self.console.print(f"[red]Error: {e}[/red]")
            self.result_display.setPlainText(f"[red]Error: {e}[/red]")