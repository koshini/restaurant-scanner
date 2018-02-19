import math


class TextAnalyzer:
    def __init__(self, corpus, text_dict, n):
        from textblob import TextBlob
        self.corpus_blob = []
        for doc in corpus:
            self.corpus_blob.append(TextBlob(doc))
        self.blob_dict = {}
        self.keyword_dict = {}
        for _id, text in text_dict.items():
            blob = TextBlob(text)
            self.blob_dict[_id] = blob
            self.keyword_dict[_id] = self.extract_words(n, blob)

    def tf(self, word, blob):
        return blob.words.count(word) / len(blob.words)

    def n_containing(self, word):
        return sum(1 for blob in self.corpus_blob if word in blob)

    def idf(self, word):
        return math.log(len(self.corpus_blob) / (1 + self.n_containing(word)))

    def tfidf(self, word, blob):
        return self.tf(word, blob) * self.idf(word)

    def extract_words(self, n, blob):
        scores = {word: self.tfidf(word, blob) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]

