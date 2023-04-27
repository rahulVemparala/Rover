"""
This is a sample Flask app that demonstrates basic functionality.

Usage:
- Run `python main.py` to start the app.
- Visit http://localhost:5000/ in your web browser to see the app in action.

Endpoints:
- `/`: Displays a welcome message.
- `/hello/<name>`: Displays a personalized greeting for the specified name.

"""


from flask import Flask, render_template

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

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
