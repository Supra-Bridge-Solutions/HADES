import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel
from PyQt5.QtGui import QPixmap
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

        self.setStyleSheet("background-color: #5C554E;")  

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.init_tabs()

        # Add watermark logo
        self.add_watermark()

    def init_tabs(self):
        self.scraper_tab = ScraperTab()
        self.scanner_tab = ScannerTab()
        self.detector_tab = DetectorTab()
        self.report_tab = ReportTab()

        self.tabs.addTab(self.scraper_tab, "Web Scraper")
        self.tabs.addTab(self.scanner_tab, "Vulnerability Scanner")
        self.tabs.addTab(self.detector_tab, "Malicious URL Detector")
        self.tabs.addTab(self.report_tab, "Generate Report")

    def add_watermark(self):
        # Create a QLabel for the watermark
        self.watermark_label = QLabel(self)
        self.watermark_label.setAlignment(Qt.AlignCenter)

        # Load the watermark image
        pixmap = QPixmap("/utils/Untitled_design.png")  # Replace with the path to your logo
        self.watermark_label.setPixmap(pixmap)

        # Resize the QLabel to fit the window
        self.watermark_label.setGeometry(0, 0, self.width(), self.height())
        self.watermark_label.setScaledContents(True)
        self.watermark_label.setStyleSheet("opacity: 0.2;")  # Optional: Make it semi-transparent

        # Ensure the watermark stays in the background
        self.watermark_label.lower()

        # Update watermark size on window resize
        self.resizeEvent = self.update_watermark_size

    def update_watermark_size(self, event):
        self.watermark_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())