"""
This is a sample Flask app that demonstrates basic functionality.

Usage:
- Run `python main.py` to start the app.
- Visit http://localhost:5000/ in your web browser to see the app in action.

Endpoints:
- `/`: Displays a welcome message.
- `/hello/<name>`: Displays a personalized greeting for the specified name.

"""


from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# setting this to prevent from modifying cookies, site attacks during register/login page
# Secretkey :  produced using secrets lib, random num
app.config['SECRET_KEY'] = "ea8af9fdf1f57149062f3985e62114b4"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///site.db'


db = SQLAlchemy(app=app)

# tables in SQLAlchemy are structured as classes in python , to work with them with ease


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


if __name__ == "__main__":
    app.run(debug=True)
