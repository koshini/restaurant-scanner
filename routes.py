from flask import Flask, render_template, request, json
from forms import SearchForm
from zomato_api.zomato import Zomato


app = Flask(__name__)
zomato = Zomato("5f7632921d92718b8c1cc580668bbd47")


@app.route("/", methods=['POST'])
def index():
    form = SearchForm()
    # Validate here
    #########################
    return render_template("index.html", form=form)


@app.route('/search', methods=['GET'])
def search():
    # Get results here
    #########################
    results = []

    # Call tf-idf module here
    #########################

    return render_template("result.html", results=results)

if __name__ == "__main__":
    app.run()
