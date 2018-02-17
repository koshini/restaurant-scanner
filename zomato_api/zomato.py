from zomato_api.requester import Requester


class Zomato():
    def __init__(self, API_KEY):
        self.r = Requester(API_KEY)

    def get_categories(self):
        categories = self.r.get('categories')
        return categories['categories']

    def get_cities(self, **kwargs):
        params = {}
        available_keys = ['q', 'lat', 'lon', 'city_ids', 'count']
        for key in available_keys:
            if key in kwargs:
                params[key] = kwargs[key]
        cities = self.r.get('cities', params)
        return cities['location_suggestions']

    def get_collections(self, city_id, **kwargs):
        params = {'city_id': city_id}
        optional_params = ['lat', 'lon', 'count']
        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        collections = self.r.get('collections', params)
        return collections

    def get_cuisines(self, city_id, **kwargs):
        params = {'city_id': city_id}
        optional_params = ['lat', 'lon']
        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        cuisines = self.r.get('cuisines', params)
        return cuisines

    def get_establishments(self, city_id, **kwargs):
        params = {'city_id': city_id}
        optional_params = ['lat', 'lon']
        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        establishments = self.r.get('establishments', params)
        return establishments


    # TO-DO:
    ######################################
    def get_location_details(self, entity_id, entity_type):
        pass

    def get_locations(self, q, **kwargs):
        params = {'query': q}
        optional_params = ['lat', 'lon', 'count']
        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        locations = self.r.get('locations', params)
        return locations

    def get_daily_menu(self, res_id):
        params = {'res_id': res_id}
        daily_menu = self.r.get('daily_menu', params)
        return daily_menu

    def get_restaurant(self, res_id):
        params = {'res_id': res_id}
        restaurant = self.r.get('restaurant', params)
        return restaurant

    def get_reviews(self, res_id, **kwargs):
        params = {'res_id': res_id}
        optional_params = ['start', 'count']
        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        reviews = self.r.get('reviews', params)
        return reviews

    def search(self,**kwargs):
        params = {}
        available_params = ['entity_id', 'entity_type', 'q', 'start', 'count', 'lat',
                            'lon', 'radius', 'cuisines', 'establishment_type',
                            'collection_id', 'category', 'sort', 'order']
        for key in available_params:
            if key in kwargs:
                params[key] = kwargs[key]
        results = self.r.get("search", params)
        return results

