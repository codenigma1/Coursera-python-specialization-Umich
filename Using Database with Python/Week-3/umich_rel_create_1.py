import sqlite3

conn = sqlite3.connect('relational.db')

cur = conn.cursor()

def create_table():
	cur.execute("CREATE TABLE IF NOT EXISTS Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Genre(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Album(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT)")
	cur.execute("CREATE TABLE IF NOT EXISTS Track(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)")


create_table()

cur.close()
conn.close()
