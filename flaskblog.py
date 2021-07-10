from flask import Flask, render_template, url_for
app = Flask(__name__)

post = [
    {
        'Author': 'Ankit',
        'title': 'Blog Post 1',
        'content': 'first post Content',
        'date_posted': 'july 4, 2021'
    },
    {
        'Author': 'Prateek',
        'title': 'Blog Post 2',
        'content': 'Second post Content',
        'date_posted': 'july 5, 2021'

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=post)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
