import unittest


class TestTextAnalyzer(unittest.TestCase):
    @staticmethod
    def do_init():
        from text_analyzer.text_analyzer import TextAnalyzer
        sample_corpus = ['foo bar foo bar bar', ' bar foo bar bar bar', 'ayy foo bar']
        t = TextAnalyzer(sample_corpus)
        return t

    def test_tf(self):
        from textblob import TextBlob
        t = self.do_init()
        blob = TextBlob('foo bar foo bar')
        tf = t.tf('foo', blob)
        self.assertEqual(tf, 0.5)

    def test_n_containing(self):
        t = self.do_init()
        n = t.n_containing('foo')
        self.assertEqual(n, 3)

    def test_idf(self):
        t = self.do_init()
        idf = t.idf('foo')
        self.assertNotEqual(idf, 0)

    def test_tfidf(self):
        from textblob import TextBlob
        t = self.do_init()
        blob = TextBlob('foo bar foo bar')
        idf = t.tfidf('foo', blob)
        self.assertNotEqual(idf, 0)

    def test_extract_words(self):
        t = self.do_init()
        words = t.extract_words(1, 'foo bar foo bar')
        self.assertEqual(len(words), 1)

    def test_remove_stopwords(self):
        from textblob import TextBlob
        t = self.do_init()
        string = 'foo this bar the bar'
        blob = t.remove_stopwords(string)
        self.assertNotIn('the', blob.words)

if __name__ == "__main__":
    unittest.main()

