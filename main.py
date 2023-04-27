"""
This is a sample Flask app that demonstrates basic functionality.

Usage:
- Run `python main.py` to start the app.
- Visit http://localhost:5000/ in your web browser to see the app in action.

Endpoints:
- `/`: Displays a welcome message.
- `/hello/<name>`: Displays a personalized greeting for the specified name.

"""


from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# Define your Flask routes and other application logic here


app = Flask(__name__)

# setting this to prevent from modifying cookies, site attacks during register/login page
# Secretkey :  produced using secrets lib, random num

app.config['SECRET_KEY'] = "ea8af9fdf1f57149062f3985e62114b4"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app=app)

# tables in SQLAlchemy are structured as classes in python , to work with them with ease


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    playlists = db.relationship('Playlist', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    songs = db.relationship('Song', backref='playlist', lazy=True)

    def __repr__(self):
        return f"Playlist('{self.title}', '{self.description}', '{self.image_file}')"


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist_name = db.Column(db.String(100), nullable=False)
    album_art_file = db.Column(
        db.String(20), nullable=False, default='default.jpg')
    playlist_id = db.Column(db.Integer, db.ForeignKey(
        'playlist.id'), nullable=False)

    def __repr__(self):
        return f"Song('{self.title}', '{self.artist_name}', '{self.album_art_file}')"


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


def create_user(**kwargs):
    with app.app_context():
        new_user = User(**kwargs)
        db.session.add(new_user)
        db.session.commit()


def view_all_users():
    with app.app_context():
        print(User.query.all())


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
    # app.run(debug=True)
    # create_user(username='johndoe', email='johndoe@example.com',
    #             password='mysecretpassword')
    view_all_users()
