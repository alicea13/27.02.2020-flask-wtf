from flask import Flask, render_template


app = Flask(__name__)


@app.route("/training/<prof>")
def prof(prof):
    if 'строитель' in prof or 'инженер' in prof:
        head_1 = 'Инженерные тренажеры'
        trace = "static/img/ing.png"
        return render_template("base.html", title=head_1, picture_name=trace)
    else:
        head_2 = "Научнык стимуляторы"
        trace = "static/img/sci.png"
        return render_template("base.html", title=head_2, picture_name=trace)
    


if __name__ == "__main__":
    app.run("", 8080)