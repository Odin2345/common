from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/author')
def get_author_page():
    return render_template("author.html", data=get_data())


@app.route('/alarm_clock')
def get_alarm_clock_page():
    return render_template("alarm_clock.html", data=get_data())


@app.route('/battery_charger')
def get_battery_charger_page():
    return render_template("battery_charger.html", data=get_data())


@app.route('/calculator')
def get_calculator_page():
    return render_template("calculator.html", data=get_data())


@app.route('/coffee_maker')
def get_coffee_maker_page():
    return render_template("coffee_maker.html", data=get_data())


@app.route('/headphones')
def get_headphones_page():
    return render_template("headphones.html", data=get_data())


@app.route('/ipod')
def get_ipod_page():
    return render_template("ipod.html", data=get_data())


if __name__ == "__main__":
    app.run(debug=True)
