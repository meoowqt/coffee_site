from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def index():
    return render_template("coffee_site/index.html")

@app.route('/comments')
def comments():
    return render_template('coffee_site/comments.html')

@app.route('/delivery')
def delivery():
    return render_template('coffee_site/delivery.html')

@app.route('/menu')
def menu():
    return render_template('coffee_site/menu.html')

@app.route('/vacancy')
def vacancy():
    return render_template('coffee_site/vacancy.html')

@app.route('/sale')
def sale():
    return render_template('coffee_site/sale.html')

@app.route('/partners')
def partners():
    return render_template('coffee_site/partners.html')
