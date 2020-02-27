from flask import Flask, render_template
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
@app.route("/index")
def index():
    args = {}
    args["username"] = "Student Yandex"
    args["title"] = "Домашняя страница"
    return render_template("index.html", **args)


@app.route("/odd_even")
def odd_even():
    return render_template('odd_even.html', number=2)


@app.route("/news")
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template("news.html", news=news_list)


@app.route("/order")
def order():
    return render_template('order.html')


if __name__ == "__main__":
    app.run('', 8080)
