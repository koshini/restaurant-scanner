import unittest


class TestTextAnalyzer(unittest.TestCase):
    @staticmethod
    def do_init():
        from text_analyzer_helper.text_analyzer import TextAnalyzer
        sample_list = ['foo bar foo bar bar. bar foo bar. bar bar', 'ayy foo bar']
        t = TextAnalyzer(sample_list)
        return t

    def test_tf(self):
        t = self.do_init()
        tf = t.tf('foo', t.sentences[0])
        self.assertEqual(tf, 0.4)

    def test_n_containing(self):
        t = self.do_init()
        n = t.n_containing('foo',)
        self.assertEqual(n, 2)

    def test_idf(self):
        t = self.do_init()
        idf = t.idf('foo')
        self.assertNotEqual(idf, 0)

    def test_tfidf(self):
        t = self.do_init()
        idf = t.tfidf('foo', t.sentences[0])
        self.assertNotEqual(idf, 0)

    #
    # def test_get_all_categories(self):
    #     t = self.do_init()
    #     category = z.get_categories()[0]['categories']
    #     self.assertEqual(category['id'], 1)
    #     self.assertEqual(category['name'], 'Delivery')
    #
    # def test_get_cities(self):
    #     z = self.do_init()
    #     city = z.get_cities(q='toronto')[0]
    #     self.assertEqual(city['id'], 89)
    #     self.assertEqual(city['country_id'], 37)
    #     self.assertEqual(city['name'], 'Toronto, ON')
    #     self.assertEqual(city['country_name'], 'Canada')
    #
    # def test_get_collections(self):
    #     z = self.do_init()
    #     collection = z.get_collections(5)
    #     self.assertIsNotNone(collection)
    #
    # def test_get_establishments(self):
    #     z = self.do_init()
    #     results = z.get_establishments(5)
    #     self.assertIsNotNone(results)
    #
    # def test_get_cuisines(self):
    #     z = self.do_init()
    #     results = z.get_cuisines(5)
    #     self.assertIsNotNone(results)
    #
    # def test_get_locations(self):
    #     z = self.do_init()
    #     results = z.get_locations("toronto")
    #     self.assertAlmostEqual(results['status'], "success")
    #
    # def test_get_location_details(self):
    #     z = self.do_init()
    #     results = z.get_location_details(3, "city")
    #     self.assertIsNotNone(results)
    #
    # def test_get_restaurant(self):
    #     z = self.do_init()
    #     restaurants = z.get_restaurant(8910284)
    #     self.assertIsNotNone(restaurants)
    #
    # def test_get_reviews(self):
    #     z = self.do_init()
    #     reviews = z.get_reviews(8910284)
    #     self.assertIsNotNone(reviews)
    #
    # def test_search(self):
    #     z = self.do_init()
    #     results = z.search(q="toronto")
    #     self.assertIsNotNone(results)

if __name__ == "__main__":
    unittest.main()

