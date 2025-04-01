import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


import joblib

class URLClassifier:
    def __init__(self):
        self.model = None

    def load_model(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, urls):
        if self.model is None:
            raise Exception("Model not loaded. Please load the model before prediction.")
        return self.model.predict(urls)