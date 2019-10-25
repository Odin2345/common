from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_home_page():
    return render_template("home.html")


@app.route("/vegetables")
def get_vegetables_page():
    list_vegetables = ["beans", "carrot", "beetroot", "cucumber"]
    return render_template("vegetables.html", list_vegetables=list_vegetables)


@app.route("/fruits")
def get_fruits_page():
    list_fruits = ["melon", "apple", "strawberry", "grape"]
    return render_template("fruits.html", list_fruits=list_fruits)


if __name__ == "__main__":
    app.run(debug=True)
