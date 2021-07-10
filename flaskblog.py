from flask import Flask, render_template, url_for
from forms import RegistartionForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '24ee0c10cc86e98d7eb9fcc08611d46b'

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


@app.route("/register")
def register():
    form = RegistartionForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
