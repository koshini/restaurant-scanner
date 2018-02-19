from zomato_api.zomato import Zomato
from text_analyzer.text_analyzer import TextAnalyzer
from zomato_api.data_preparation_helper import DataPreparationHelper



def main():
    # zomato = Zomato("5f7632921d92718b8c1cc580668bbd47")
    zomato = Zomato("29d2f8d3ea12fe6d7234f71240aecc38")
    data_preparation_helper = DataPreparationHelper()
    # cities = zomato.get_cities(q='toronto')
    locations = zomato.get_locations('toronto')
    id, type = data_preparation_helper.parse_locations(locations)
    category = zomato.get_categories()
    results = zomato.search(entity_id=id, entity_type=type, cuisines=308, sort='rating', order='desc')
    corpus = []
    corpus_results = zomato.search(entity_id=id, entity_type=type, sort='rating', order='desc')
    for res in corpus_results['restaurants']:
        reviews = zomato.get_reviews(res_id=res['restaurant']['id'])
        if len(reviews['user_reviews']) > 0:
            corpus.append(data_preparation_helper.get_review_text(reviews['user_reviews']))
    review_analyzer = TextAnalyzer(corpus)


    reviews = zomato.get_reviews(res_id=results['restaurants'][0]['restaurant']['id'])
    review_text = data_preparation_helper.get_review_text(reviews['user_reviews'])
    keywords = review_analyzer.extract_words(5, review_text)

    pass




if __name__ == "__main__":
    main()