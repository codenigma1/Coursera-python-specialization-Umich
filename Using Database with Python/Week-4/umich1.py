import sqlite3

conn = sqlite3.connect('week4db.db')

cur = conn.cursor()

def create_table():
	cur.execute("CREATE TABLE IF NOT EXISTS User(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, email TEXT)")

	cur.execute("CREATE TABLE IF NOT EXISTS Course(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT)")

	cur.execute("CREATE TABLE IF NOT EXISTS Member(user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY(user_id, course_id))")

create_table()

def data_entry():
	cur.execute("INSERT INTO User(name, email) VALUES ('Jane', 'jane@tsugi.org'), ('Ed', 'ed@tsugi.org'), ('Sue', 'sue@tsugi.org')")

	cur.execute("INSERT INTO Course(title) VALUES ('Python'), ('SQL'), ('PHP')")

	cur.execute("INSERT INTO Member(user_id, course_id, role) VALUES (1,1,1), (2,1,0), (3,1,0), (1,2,0), (2,2,1), (2,3,1), (3,3,0)")	

	conn.commit()

data_entry()

cur.close()
conn.close()