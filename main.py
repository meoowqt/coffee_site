from flask import Flask, render_template, request, flash, redirect
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:1234@localhost:5432/postgres"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Comment(db.Model):
    __tablename__ = "comment"

    comment_id = db.Column(
        db.Integer(), primary_key=True, nullable=False, autoincrement=True
    )
    comment_text = db.Column(db.Text(), nullable=False)
    commentator_name = db.Column(db.Text(), nullable=False)

    def __init__(self, _name, _text):
        self.commentator_name = _name
        self.comment_text = _text


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    context = {
        "title": "Главная страница",
    }
    return render_template("coffee_site/index.html", context=context)


@app.route("/comments", methods=["POST", "GET"])
def comments():
    context = {
        "title": "Отзывы",
    }
    if request.method == ["POST"]:
        name = request.form["name"]
        text = request.form["text"]
        comm = Comment(_text=text, _name=name)
        db.session.add(comm)
        db.session.commit()
    comms = Comment.query.order_by(desc(Comment.comment_id)).all()
    return render_template("coffee_site/comments.html", context=context)


@app.route("/delivery")
def delivery():
    context = {
        "title": "Доставка",
    }
    return render_template("coffee_site/delivery.html", context=context)


@app.route("/menu")
def menu():
    context = {
        "title": "Меню - Каталог",
    }
    return render_template("coffee_site/menu.html", context=context)


@app.route("/vacancy")
def vacancy():
    context = {
        "title": "Вакансии",
    }
    return render_template("coffee_site/vacancy.html", context=context)


@app.route("/sale")
def sale():
    context = {
        "title": "Акции и скидки",
    }
    return render_template("coffee_site/sale.html", context=context)


@app.route("/partners")
def partners():
    context = {
        "title": "Партнерам",
    }
    return render_template("coffee_site/partners.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)
