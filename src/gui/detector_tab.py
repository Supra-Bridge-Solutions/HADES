
import sys
sys.path.append('/opt/lampp/htdocs/projects/HADES/src/models')
from models.malicious_url_classifier import URLClassifier

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class DetectorTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter URL to classify")
        self.layout.addWidget(self.url_input)

        self.classify_button = QPushButton("Classify URL", self)
        self.classify_button.clicked.connect(self.classify_url)
        self.layout.addWidget(self.classify_button)

        self.result_label = QLabel(self)
        self.layout.addWidget(self.result_label)

        self.classifier = URLClassifier()

    def classify_url(self):
        url = self.url_input.text().strip()
        try:
            result = self.classifier.classify(url)
            self.result_label.setText(f"Classification: {result}")
        except Exception as e:
            self.result_label.setText(f"Error: {e}")