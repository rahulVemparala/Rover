"""
routes for our website

"""

from flask import render_template, url_for, flash, redirect

from rover.forms import RegistrationForm, LoginForm

from main import app


posts = [
    {
        "artist_name": "Usher Raymond",
        "country": "American",
        "songs": ['My Boo', 'Dive', 'U Remind me']
    },

    {
        "artist_name": "Kai of EXO",
        "country": "Korean",
        "songs": ['Vanilla', 'Peaches', 'Rover']
    },

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/signout")
def signout():
    return render_template('signout.html', title='About')


@app.route("/register", methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            message=f"Account created for {form.username.data}", category='success')
        return redirect(url_for('home'))
    return render_template('register2.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass

    return render_template('login.html', title='Register', form=form)
