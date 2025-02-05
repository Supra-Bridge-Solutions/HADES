import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

class URLClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = LogisticRegression()