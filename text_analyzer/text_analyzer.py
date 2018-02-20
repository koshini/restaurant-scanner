import math
from textblob import TextBlob

class TextAnalyzer:
    def __init__(self, corpus):
        self.corpus_blob = []
        for doc in corpus:
            blob = self.remove_stopwords(doc)
            self.corpus_blob.append(blob)


    def tf(self, word, blob):
        return blob.words.count(word) / len(blob.words)

    def n_containing(self, word):
        return sum(1 for blob in self.corpus_blob if word in blob)

    def idf(self, word):
        return math.log(len(self.corpus_blob) / (1 + self.n_containing(word)))

    def tfidf(self, word, blob):
        return self.tf(word, blob) * self.idf(word)

    def extract_words(self, n, text):
        blob = self.remove_stopwords(text)
        scores = {word: self.tfidf(word, blob) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]

    def remove_stopwords(self, string):
        from nltk.corpus import stopwords
        string = string.split()
        useful_words = [w for w in string if w not in set(stopwords.words("english"))]
        useful_words = ' '.join(useful_words)
        blob = TextBlob(useful_words)
        return blob
