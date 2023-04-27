"""
routes for our website

"""

from flask import render_template, url_for, flash, redirect

from rover.forms import RegistrationForm, LoginForm

from rover import app, db, bcrypt

from rover.database import User
from flask_login import login_user, current_user, logout_user

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


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/register", methods=['GET', "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        create_user(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password
                    )

        flash(
            message=f"Account created for {form.username.data}!", category='success')
        return redirect(url_for('login'))
    return render_template('register2.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccesful, please check Email or Password.",
                  category="error")
    return render_template('login.html', title='Login', form=form)


def create_user(**kwargs):
    with app.app_context():
        new_user = User(**kwargs)
        db.session.add(new_user)
        db.session.commit()


def view_all_users():
    with app.app_context():
        print(User.query.get_all())
