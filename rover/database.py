"""

ORM files, or classes that are similar to db tables
"""

from datetime import datetime
from rover import db
from rover import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    playlists = db.relationship('Playlist', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    artists = db.relationship('Artist', backref='genre', lazy=True)

    def __repr__(self):
        return f"Genre('{self.name}', '{self.image_file}')"


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    albums = db.relationship('Album', backref='artist', lazy=True)
    playlists = db.relationship(
        'Playlist', secondary='playlist_artists', backref='artists', lazy=True)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    image_path = db.Column(db.String(100), nullable=False,
                           default='static/artist_pics')


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'artist.id'), nullable=False)
    release_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    songs = db.relationship('Song', backref='album', lazy=True)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    image_path = db.Column(db.String(100), nullable=False,
                           default='static/album_pics')


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    songs = db.relationship(
        'Song', secondary='playlist_songs', backref='playlists', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    image_path = db.Column(db.String(100), nullable=False,
                           default='static/playlist_pics')


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))
    file_path = db.Column(db.String(200), nullable=False)


playlist_songs = db.Table('playlist_songs',
                          db.Column('playlist_id', db.Integer, db.ForeignKey(
                              'playlist.id'), primary_key=True),
                          db.Column('song_id', db.Integer, db.ForeignKey(
                              'song.id'), primary_key=True)
                          )

playlist_artists = db.Table('playlist_artists',
                            db.Column('playlist_id', db.Integer, db.ForeignKey(
                                'playlist.id'), primary_key=True),
                            db.Column('artist_id', db.Integer, db.ForeignKey(
                                'artist.id'), primary_key=True)
                            )
