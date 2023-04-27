"""

ORM files, or classes that are similar to db tables
"""
from rover import db


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
