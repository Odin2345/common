from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data(), title="Home")


@app.route('/author')
def get_author_page():
    return render_template("author.html", data=get_data(), title="Author")


@app.route('/alarm_clock')
def get_alarm_clock_page():
    return render_template("product.html", data=get_data(), title="Alarm clock")


@app.route('/battery_charger')
def get_battery_charger_page():
    return render_template("product.html", data=get_data(), title="Battery charger")


@app.route('/calculator')
def get_calculator_page():
    return render_template("product.html", data=get_data(), title="Calculator")


@app.route('/coffee_maker')
def get_coffee_maker_page():
    return render_template("product.html", data=get_data(), title="Coffeemaker")


@app.route('/headphones')
def get_headphones_page():
    return render_template("product.html", data=get_data(), title="Headphones")


@app.route('/ipod')
def get_ipod_page():
    return render_template("product.html", data=get_data(), title="iPod")


if __name__ == "__main__":
    app.run(debug=True)
