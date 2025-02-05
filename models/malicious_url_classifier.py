import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

class URLClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = LogisticRegression()

    def train(self, urls, labels):
        X = self.vectorizer.fit_transform(urls)
        self.model.fit(X, labels)

    def predict(self, urls):
        X = self.vectorizer.transform(urls)
        return self.model.predict(X)
    
    def save_model(self, filepath):
        with open(filepath, "wb") as f:
            pickle.dump({"model": self.model, "vectorizer": self.vectorizer}, f)

    def load_model(self, filepath):
        with open(filepath, "rb") as f:
            data = pickle.load(f)
            self.model = data["model"]
            self.vectorizer = data["vectorizer"]


if __name__ == "__main__":
    urls = ["http://safe-site.com", "http://malicious-site.xyz"]
    labels = [0, 1]  # 0: Safe, 1: Malicious

    classifier = URLClassifier()
    classifier.train(urls, labels)
    classifier.save_model("models/url_classifier.pkl")
    print("[INFO] Model trained and saved.")