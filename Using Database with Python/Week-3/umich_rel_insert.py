import sqlite3

conn = sqlite3.connect('relational.db')

cur = conn.cursor()

def create_table():
	cur.execute("CREATE TABLE IF NOT EXISTS Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Genre(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Album(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Track(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)")

# create_table()

def data_entry():
	cur.execute("INSERT INTO Artist(name) VALUES ('Led Zepplin'), ('AC/DC')");
	cur.execute("INSERT INTO Genre(name) VALUES ('Rock'), ('Metal')");
	cur.execute("INSERT INTO Album(title, artist_id) VALUES ('Who Made Who', 2), ('IV', 1)");
	cur.execute("INSERT INTO Track(title, album_id, genre_id, len, rating, count) VALUES ('Black Dog', 5, 297,0, 2, 1), ('Stairway', 5, 482, 0, 2, 1), ('About to Rock', 5, 313, 0, 1, 2), ('Who Made Who', 5, 207, 0, 1, 2)")

	# conn.commit()


# Here I used JOIN simple query.
def select_data():
	# cur.execute("SELECT Album.title, Artist.name, Album.artist_id, Artist.id  FROM Artist JOIN Album WHERE Album.artist_id=Artist.id")

	cur.execute("SELECT Track.title, Artist.name,Album.title, Genre.name FROM Track JOIN Genre JOIN Artist JOIN Album WHERE Track.genre_id=Genre.id AND Album.id=Track.album_id AND Artist.id=Album.artist_id")

	print(cur.fetchall())

select_data()
# data_entry()

cur.close()
conn.close()