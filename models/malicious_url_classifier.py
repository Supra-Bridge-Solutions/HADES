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