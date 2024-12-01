from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class TfidfEmbeddings:
    def __init__(self):
        # Initialize TfidfVectorizer with optional parameters
        self.vectorizer = TfidfVectorizer(stop_words='english', min_df=1)  # Removes stop words and considers all terms that appear at least once
        self.vectors = None

    def fit(self, texts):
        if not texts or all(text.strip() == '' for text in texts):
            raise ValueError("Input texts are empty or only contain whitespace.")
        self.vectorizer.fit(texts)

    def embed_documents(self, texts):
        if not hasattr(self.vectorizer, 'vocabulary_'):
            raise ValueError("Vectorizer not fitted. Call fit() before embedding documents.")
        if not texts or all(text.strip() == '' for text in texts):
            raise ValueError("Input texts are empty or only contain whitespace.")
        return self.vectorizer.transform(texts).toarray()

    def embed_query(self, text):
        if not hasattr(self.vectorizer, 'vocabulary_'):
            raise ValueError("Vectorizer not fitted. Call fit() before embedding query.")
        if text.strip() == '':
            raise ValueError("Input query is empty.")
        return self.vectorizer.transform([text]).toarray()[0]

    def __call__(self, text):
        # This method makes the class callable
        if isinstance(text, str):
            return self.embed_query(text)
        elif isinstance(text, list):
            return self.embed_documents(text)
        else:
            raise ValueError("Input must be a string or a list of strings")

    def embed_many(self, texts):
        # Alias for embed_documents to match expected interface
        return self.embed_documents(texts)
