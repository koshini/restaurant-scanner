from flask import Flask, render_template, request, jsonify
from forms import SearchForm
from zomato_api.zomato import Zomato
from zomato_api.data_preparation_helper import DataPreparationHelper
from text_analyzer.text_analyzer import TextAnalyzer


app = Flask(__name__)
zomato = Zomato("YOUR_API_KEY")

app.secret_key = 'development-key'


@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    # validate_on_submit will check if it is a POST request and if it is valid.
    if not form.validate_on_submit():
        print("Invalid input")
        return render_template("search.html", form=form)
    elif request.method == 'POST':
        return result(form)

@app.route('/result')
def result(form):
    data_preparation_helper = DataPreparationHelper()
    # Get input from form
    location = str(form.location.data)

    # Query from Zomato API
    #########################
    locations = zomato.get_locations(location)
    id, type = data_preparation_helper.parse_locations(locations)
    results = zomato.search(entity_id=id, entity_type=type, cuisines=308, count=5, sort='rating', order='desc')
    restaurants = data_preparation_helper.results_clean_up(results)

    # Apply tfidf algorithm to reviews
    #########################

    # Get reviews from all types pf restaurants at the same location as corpus
    corpus = []
    corpus_results = zomato.search(entity_id=id, entity_type=type)
    keyword_dict = {}
    for res in corpus_results['restaurants']:
        reviews = zomato.get_reviews(res_id=res['restaurant']['id'])
        if len(reviews['user_reviews']) > 0:
            corpus.append(data_preparation_helper.get_review_text(reviews['user_reviews']))
    review_analyzer = TextAnalyzer(corpus)
    for _id, res in restaurants.items():
        reviews = zomato.get_reviews(_id)
        if len(reviews['user_reviews']) > 0:
            review_text = data_preparation_helper.get_review_text(reviews['user_reviews'])
            keyword_dict[_id] = review_analyzer.extract_words(5, review_text)

    return render_template("result.html", restaurants=restaurants, keyword_dict=keyword_dict)

# @app.route('/scan_reviews')
# def scan_reviews(review_analyzer):
#     try:
#         res_id = request.args.get('res_id')
#         reviews = zomato.get_reviews(res_id)
#         data_preparation_helper = DataPreparationHelper()
#         review_text = data_preparation_helper.get_review_text(reviews['user_reviews'])
#         keywords = review_analyzer.extract_words(5, review_text)
#         return keywords
#     except Exception as e:
#         return str(e)

if __name__ == "__main__":
    app.run()
