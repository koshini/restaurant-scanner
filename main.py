from zomato_api.zomato import Zomato
from textblob import TextBlob as tb
from text_analyzer_helper.text_analyzer import TextAnalyzer



def main():
    zomato = Zomato("5f7632921d92718b8c1cc580668bbd47")
    # cities = zomato.get_cities(q='toronto')
    locations = zomato.get_locations('toronto')
    id, type = parse_locations(locations)
    category = zomato.get_categories()
    results = zomato.search(entity_id=id, entity_type=type, cuisines=308)
    review_dict = {}
    review_text_dict = {}
    for restaurant in results['restaurants']:
        reviews = zomato.get_reviews(res_id=restaurant['restaurant']['id'])
        review_dict[restaurant['restaurant']['id']] = reviews['user_reviews']
        review_text_dict[restaurant['restaurant']['id']] = get_review_text(reviews['user_reviews'])


    # corpus is the list reveiws of a results = zomato.search(entity_id=id, entity_type=type)
    corpus = []
    review_analyzer = TextAnalyzer(corpus, review_text_dict, 10)
    pass


def parse_locations(locations):
    location = locations['location_suggestions'][0]
    return location['entity_id'], location['entity_type']

def get_review_text(review_list):
    text = ''
    for review in review_list:
        text = text + review['review']['review_text']
    return text


if __name__ == "__main__":
    main()