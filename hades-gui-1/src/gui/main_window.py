import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from scraper_tab import ScraperTab
from scanner_tab import ScannerTab
from detector_tab import DetectorTab
from report_tab import ReportTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HADES - AI Cyber Recon Toolkit")
        self.setGeometry(100, 100, 800, 600)

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