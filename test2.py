from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run('', 8080)
