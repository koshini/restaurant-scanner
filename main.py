from zomato_api.zomato import Zomato

def main():
    zomato = Zomato("5f7632921d92718b8c1cc580668bbd47")
    cities = zomato.get_cities(q='toronto')
    locations = zomato.get_locations('toronto')
    id, type = parse_locations(locations)
    category = zomato.get_categories()
    results = zomato.search(entity_id=id, entity_type=type, cuisines=308)
    review_dict ={}
    for restaurant in results['restaurants']:
        reviews = zomato.get_reviews(res_id=restaurant['restaurant']['id'])
        review_dict[restaurant['restaurant']['id']] = reviews
    pass

def parse_locations(locations):
    location = locations['location_suggestions'][0]
    return location['entity_id'], location['entity_type']


if __name__ == "__main__":
    main()