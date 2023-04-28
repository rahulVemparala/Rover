import csv
import re
from rover import app,  db
from rover.database import Genre, Artist, Album, Song

# open the sample data CSV file
with open('sample_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # extract the album name without the year from the content column
        album_name = re.sub(r'\s*\(\d{4}\)$', '', row['Albums'])

        # get or create the Genre instance
        genre = Genre.query.filter_by(name=row['Genre']).first()
        if not genre:
            genre = Genre(name=row['Genre'], image_file=row['genre_image'])
            db.session.add(genre)

        # get or create the Artist instance
        artist = Artist.query.filter_by(name=row['Artist Name']).first()
        if not artist:
            artist = Artist(name=row['Artist Name'],
                            image_file=row['artist_image'])
            db.session.add(artist)

        # get or create the Album instance
        album = Album.query.filter_by(name=album_name).first()
        if not album:
            album = Album(name=album_name, image_file=row['album_image'], year=int(
                row['Albums'][-5:-1]))
            db.session.add(album)

        # create the Song instance
        song = Song(name=row['Songs'], album=album)
        db.session.add(song)

        # link the Genre, Artist, and Album instances
        genre.artists.append(artist)
        artist.albums.append(album)

# commit the changes to the database
db.session.commit()
