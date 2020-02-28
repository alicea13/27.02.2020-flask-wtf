from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
# @app.route("/index/<title>")
# def index(title):
    # return render_template("base.html", title=title)


@app.route("/list_prof/<list>")
def list_prof(list):
    return render_template("profi.html", par=list)


if __name__ == "__main__":
    app.run('', 8080)
