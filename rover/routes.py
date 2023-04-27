"""
routes for our website

"""

from flask import render_template, url_for, flash, redirect

from rover.forms import RegistrationForm, LoginForm

from rover import app, db, bcrypt

from rover.database import User

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
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        create_user(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password
                    )

        flash(
            message=f"Account created for {form.username.data}!", category='success')
        return redirect(url_for('home'))
    return render_template('register2.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass

    return render_template('login.html', title='Register', form=form)


def create_user(**kwargs):
    with app.app_context():
        new_user = User(**kwargs)
        db.session.add(new_user)
        db.session.commit()


def view_all_users():
    with app.app_context():
        print(User.query.get_all())
