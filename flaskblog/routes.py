from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistartionForm, LoginForm
from flaskblog.models import User, Post


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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistartionForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", category="success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
