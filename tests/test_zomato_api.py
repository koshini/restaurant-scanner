import unittest


class TestZomato(unittest.TestCase):
    @staticmethod
    def do_init():
        from zomato_api.zomato import Zomato
        z = Zomato(API_KEY="5f7632921d92718b8c1cc580668bbd47")
        return z

    def test_get_all_categories(self):
        z = self.do_init()
        category = z.get_categories()[0]['categories']
        self.assertEqual(category['id'], 1)
        self.assertEqual(category['name'], 'Delivery')

    def test_get_cities(self):
        z = self.do_init()
        city = z.get_cities(q='toronto')[0]
        self.assertEqual(city['id'], 89)
        self.assertEqual(city['country_id'], 37)
        self.assertEqual(city['name'], 'Toronto, ON')
        self.assertEqual(city['country_name'], 'Canada')

    def test_get_collections(self):
        z = self.do_init()
        collection = z.get_collections(5)
        self.assertIsNotNone(collection)

    def test_get_establishments(self):
        z = self.do_init()
        results = z.get_establishments(5)
        self.assertIsNotNone(results)

    def test_get_cuisines(self):
        z = self.do_init()
        results = z.get_cuisines(5)
        self.assertIsNotNone(results)

    def test_get_locations(self):
        z = self.do_init()
        results = z.get_locations("toronto")
        self.assertAlmostEqual(results['status'], "success")

    def test_get_location_details(self):
        z = self.do_init()
        results = z.get_location_details(3, "city")
        self.assertIsNotNone(results)

    def test_get_restaurant(self):
        z = self.do_init()
        restaurants = z.get_restaurant(8910284)
        self.assertIsNotNone(restaurants)

    def test_get_reviews(self):
        z = self.do_init()
        reviews = z.get_reviews(8910284)
        self.assertIsNotNone(reviews)

    def test_search(self):
        z = self.do_init()
        results = z.search(q="toronto")
        self.assertIsNotNone(results)

if __name__ == "__main__":
    unittest.main()

