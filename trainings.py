from flask import Flask, render_template


app = Flask(__name__)


@app.route("/training/<prof>")
def prof(prof):
    if 'строитель' in prof or 'инженер' in prof:
        head_1 = 'Инженерные тренажеры'
        return render_template("base.html", title=head_1)
    


if __name__ == "__main__":
    app.run("", 8080)