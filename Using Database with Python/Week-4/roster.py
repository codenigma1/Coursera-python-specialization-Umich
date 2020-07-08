import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')

cur = conn.cursor()


def drop_table():
	cur.execute("DROP TABLE IF EXISTS User")
	cur.execute("DROP TABLE IF EXISTS Member")
	cur.execute("DROP TABLE IF EXISTS Course")

drop_table()

def create_table():
	cur.execute("CREATE TABLE IF NOT EXISTS User(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)")

	cur.execute("CREATE TABLE IF NOT EXISTS Course(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE)")

	cur.execute("CREATE TABLE IF NOT EXISTS Member(user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY(user_id, course_id))")

create_table()

fhand = input("Enter the file name: ")
str_data = open(fhand).read()
json_data = json.loads(str_data)

for entry in json_data:
	name = entry[0]
	title = entry[1]
	role = entry[2]

	print('Name: ', name, 'Title: ', title, 'Role: ', role)

	cur.execute("INSERT OR IGNORE INTO User(name) VALUES (?)", (name, ))
	cur.execute("SELECT id FROM User WHERE name = ?", (name, ))
	user_id = cur.fetchone()[0]

	cur.execute("INSERT OR IGNORE INTO Course(title) VALUES (?)", (title, ))
	cur.execute("SELECT id FROM Course WHERE title = ?", (title, ))
	course_id = cur.fetchone()[0]

	cur.execute("INSERT OR IGNORE INTO Member(user_id, course_id, role) VALUES (?,?,?)", (user_id, course_id, role))
	
	conn.commit()

cur.close()
conn.close()




