from datetime import timedelta
from flask import Flask, render_template, session
from config import Config
from blueprint.products.product_main import products
from blueprint.supermarket.supermarket_main import supermarket

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(products)
app.register_blueprint(supermarket)
app.permanent_session_lifetime = timedelta(seconds=10)


@app.route("/")
def get_home_page():
    session['login'] = 'ok'
    return render_template("home.html", title='Home')


@app.errorhandler(404)
def get_error_page(error):
    return render_template("error_404.html", title='Error 404'), 404


if __name__ == "__main__":
    app.run()
