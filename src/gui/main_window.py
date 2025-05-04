import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from src.gui.scraper_tab import ScraperTab
from src.gui.scanner_tab import ScannerTab
from src.gui.detector_tab import DetectorTab
from src.gui.report_tab import ReportTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HADES - AI Cyber Recon Toolkit")
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet("background-color: #7e7b7a;")  

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.init_tabs()

    def init_tabs(self):
        self.scraper_tab = ScraperTab()
        self.scanner_tab = ScannerTab()
        self.detector_tab = DetectorTab()
        self.report_tab = ReportTab()

        self.tabs.addTab(self.scraper_tab, "Web Scraper")
        self.tabs.addTab(self.scanner_tab, "Vulnerability Scanner")
        self.tabs.addTab(self.detector_tab, "Malicious URL Detector")
        self.tabs.addTab(self.report_tab, "Generate Report")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())