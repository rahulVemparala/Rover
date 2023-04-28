import pandas as pd
from rover import app, db
from rover.database import Genre, Artist, Album, Song


def reset_db():

    with app.app_context():
        db.drop_all()


def init_db():
    with app.app_context():
        db.create_all()


def insert_db():
    # read data from CSV file
    df = pd.read_csv('sample_data.csv')

    # remove date from album name using regex
    df['Albums'] = df['Albums'].str.replace(r'\s*\(\d{4}\)', '', regex=True)

    # insert data into database
    for _, row in df.iterrows():
        # get or create genre
        genre = Genre.query.filter_by(name=row['Genre']).first()
        if not genre:
            genre = Genre(name=row['Genre'], image_file=row['genre_image'])
            db.session.add(genre)

        # get or create artist
        artist = Artist.query.filter_by(name=row['Artist Name']).first()
        if not artist:
            artist = Artist(name=row['Artist Name'],
                            image_file=row['artist_image'])
            db.session.add(artist)

        # get or create album
        album = Album.query.filter_by(title=row['Albums']).first()
        if not album:
            album = Album(title=row['Albums'], year=None,
                          image_file=row['album_image'], artist=artist, genre=genre)
            db.session.add(album)

        # add song to album
        song = Song(title=row['Songs'], track_number=None,
                    length=None, album=album)
        db.session.add(song)

    # commit changes to database
    db.session.commit()


if __name__ == '__main__':
    # reset_db()
    # init_db()
    insert_db()
    # app.run(debug=True)
