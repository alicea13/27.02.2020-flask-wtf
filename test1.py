from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    args = {}
    args["username"] = "Student Yandex"
    args["title"] = "Домашняя страница"
    return render_template("index.html", **args)


if __name__ == "__main__":
    app.run('', 8080)
