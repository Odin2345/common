 from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", title="Home")


@app.route('/author')
def get_author_page():
    return render_template("author.html", title="Author")


@app.route('/<product>')
def get_product_page(product):
    data = get_data()
    for elem in data:
        if product == elem['title'].replace(' ', '_').lower():
            return render_template("product.html",
                                   title=elem['title'],
                                   src_img=elem['src_img'],
                                   text=elem['text'],
                                   wiki_url=elem['wiki_url'])


if __name__ == "__main__":
    app.run(debug=True)
