import pandas as pd
import uuid
from datetime import datetime
from rover import app, db
from rover.database import User, Genre, Artist, Album, Song, Playlist


def reset_db():

    with app.app_context():
        db.drop_all()


def init_db():
    with app.app_context():
        db.create_all()


def insert_db():
    # read data from CSV file
    data = pd.read_parquet('country.parquet')

    # Generate unique ids for each table
    genre_id = uuid.uuid4().int & (1 << 32)-1
    artist_id = uuid.uuid4().int & (1 << 32)-1
    album_id = uuid.uuid4().int & (1 << 32)-1
    song_id = uuid.uuid4().int & (1 << 32)-1
    user_id = uuid.uuid4().int & (1 << 32)-1

    # Loop through each row of the data and insert into the database
    with app.app_context():
        df = pd.read_parquet('pop.parquet')

        # # Insert genres
        genres = []
        for i, row in df.iterrows():
            genre_name = row['genre']
            genre_image = row['genre_image']
            genre = Genre(name=genre_name, image_file=genre_image)
            genres.append(genre)
        db.session.add_all(genres)
        db.session.commit()

        # # Insert artists
        artists = []
        for i, row in df.iterrows():
            artist_name = row['artist_name']
            artist_image = row['artist_image']
            genre_name = row['genre']
            genre = Genre.query.filter_by(name=genre_name).first()
            if genre:
                artist = Artist(name=artist_name, genre=genre,
                                image_file=artist_image)
                artists.append(artist)
        db.session.add_all(artists)
        db.session.commit()

        # # Insert albums
        albums = []
        for i, row in df.iterrows():
            album_name = row['album']
            album_image = row['album_image']
            artist_name = row['artist_name']
            artist = Artist.query.filter_by(name=artist_name).first()
            if artist:
                album = Album(name=album_name, artist=artist,
                              image_file=album_image)
                albums.append(album)
        db.session.add_all(albums)
        db.session.commit()

        # Insert artists
        artists = []
        for i, row in df.iterrows():
            artist_name = row['artist_name']
            artist_image = row['artist_image']
            genre_name = row['genre']
            genre = Genre.query.filter_by(name=genre_name).first()
            if genre:
                artist = Artist(name=artist_name, genre=genre,
                                image_file=artist_image)
                artists.append(artist)
        db.session.add_all(artists)
        db.session.commit()

        # Insert albums
        albums = []
        for i, row in df.iterrows():
            album_name = row['album']
            album_image = row['album_image']
            artist_name = row['artist_name']
            artist = Artist.query.filter_by(name=artist_name).first()
            if artist:
                album = Album(name=album_name, artist=artist,
                              image_file=album_image)
                albums.append(album)
        db.session.add_all(albums)
        db.session.commit()

        # Insert songs
        songs = []
        for i, row in df.iterrows():
            song_name = row['songs']
            duration = 180  # Assuming all songs are 3 minutes long
            album_name = row['album']
            album = Album.query.filter_by(name=album_name).first()
            if album:
                song = Song(name=song_name, duration=duration,
                            album=album, file_path='path/to/song.mp3')
                songs.append(song)
        db.session.add_all(songs)
        db.session.commit()

        # Insert users and playlists
        # user = User(username='rahul123', email='rahul123@gmail.com',
        #             password='rahul', image_file='rahul.jpg')
        # db.session.add(user)
        # db.session.commit()

        # playlists = []
        # for i, row in df.iterrows():
        #     playlist_name = "Playlist1"
        #     playlist_desc = "Sample Playlist"

        #     songs = ['Coat of Many Colors',
        #              "Travelin' Man",
        #              'My Blue Tears',
        #              'Here You Come Again',
        #              "It's All Wrong, But It's All Right",
        #              'Me and Little Andy',
        #              'Jolene',
        #              'When Someone Wants to Leave']
        #     playlist_songs = Song.query.filter(Song.name.in_(songs)).all()
        #     if playlist_songs:
        #         playlist = Playlist(
        #             name=playlist_name, description=playlist_desc, user=user, songs=playlist_songs)
        #         playlists.append(playlist)
        # db.session.add_all(playlists)
        # db.session.commit()


if __name__ == '__main__':
    # reset_db()
    # init_db()
    # insert_db()
    app.run(debug=True)
