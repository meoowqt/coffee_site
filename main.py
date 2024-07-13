from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)


@app.route("/")
def index():
    context = {
        "title": "Главная страница",
    }
    return render_template("coffee_site/index.html", context=context)


@app.route("/comments")
def comments():
    context = {
        "title": "Отзывы",
    }
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
