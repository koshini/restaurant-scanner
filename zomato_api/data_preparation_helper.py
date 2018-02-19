class DataPreparationHelper:
    def __init__(self):
        pass

    @staticmethod
    def parse_locations(locations):
        location = locations['location_suggestions'][0]
        return location['entity_id'], location['entity_type']

    @staticmethod
    def get_review_text(review_list):
        text = ''
        for review in review_list:
            if review['review']['review_text']:
                text = text + review['review']['review_text']
        return text

    def results_clean_up(self, results):
        restaurant_list = results['restaurants']
        clean_result = {}
        for res in restaurant_list:
            res = res['restaurant']
            clean_result[res['id']] = self.remove_unwanted_fields(res)
        return clean_result

    def remove_unwanted_fields(self, res):
        res['rating'] = res['user_rating']['aggregate_rating']
        res['votes'] = res['user_rating']['votes']
        res['address'] = res['location']['address']
        keys_to_remove = ['R', 'apikey', 'deeplink', 'establishment_types', 'featured_image', 'currency',
                          'has_online_delivery', 'has_table_booking', 'is_delivering_now', 'offers',
                          'switch_to_order_menu', 'thumb', 'location', 'user_rating']
        for key in keys_to_remove:
            del res[key]
        return res

    def listify_reviews(self, reviews):
        pass