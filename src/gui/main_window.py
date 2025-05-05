import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from src.gui.scraper_tab import ScraperTab
from src.gui.scanner_tab import ScannerTab
from src.gui.detector_tab import DetectorTab
from src.gui.report_tab import ReportTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HADES - AI Cyber Recon Toolkit")
        self.setGeometry(100, 100, 800, 600)

        # REVIEW: Using a QSS (Qt Style Sheet) to set the background image as the watermark.
        # The image should be pre-processed to have reduced opacity since QSS does not support alpha for images.
        self.main_widget = QWidget(self)
        self.main_widget.setContentsMargins(0, 0, 0, 0)
        self.main_widget.setStyleSheet("""
            QWidget {
                background-color: #4F5157;  /* Fallback background color */
                background-image: url('src/utils/hades_logo_.png');  /* Path to your logo with pre-adjusted opacity */
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }
        """)
        self.setCentralWidget(self.main_widget)

        # REVIEW: Create a layout for stacking UI elements atop the background.
        self.ui_layout = QVBoxLayout(self.main_widget)
        self.ui_layout.setContentsMargins(0, 0, 0, 0)

        # REVIEW: Initialize the tabs (which will appear on top of the background watermark).
        self.init_tabs()

    def init_tabs(self):
        """
        Initializes the QTabWidget with the various application tabs.
        REVIEW:
          - Consider adding error handling if a tab fails to initialize.
          - This widget is added to the main layout so it appears over the background image.
        """
        self.tabs = QTabWidget(self)
        self.tabs.addTab(ScraperTab(), "Web Scraper")
        self.tabs.addTab(ScannerTab(), "Vulnerability Scanner")
        self.tabs.addTab(DetectorTab(), "Malicious URL Detector")
        self.tabs.addTab(ReportTab(), "Generate Report")
        self.ui_layout.addWidget(self.tabs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())