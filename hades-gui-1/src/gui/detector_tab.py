from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from models.malicious_url_classifier import URLClassifier
from src.input_handler import validate_url

class DetectorTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter URL to analyze")
        layout.addWidget(self.url_input)

        self.detect_button = QPushButton("Detect Malicious URL", self)
        self.detect_button.clicked.connect(self.detect_url)
        layout.addWidget(self.detect_button)

        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def detect_url(self):
        url = self.url_input.text().strip()
        try:
            validated_url = validate_url(url)
            classifier = URLClassifier()
            classifier.load_model("models/url_classifier.pkl")
            prediction = classifier.predict([validated_url])[0]
            status = "Malicious" if prediction == 1 else "Safe"
            self.result_display.setText(f"{validated_url}: {status}")
        except Exception as e:
            self.result_display.setText(f"Error: {e}")