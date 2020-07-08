import sqlite3

conn = sqlite3.connect("email.db")
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS Ages(name VARCHAR(128), age INTEGER)")

# create_table()

def delete_row():
	c.execute("DELETE FROM Ages")

def data_entry():
	c.execute("INSERT INTO Ages (name, age) VALUES ('Kaydyne', 21), ('Hayla', 18), ('Jahid', 39), ('Kasra', 27), ('Naisha', 40), ('Stephenjunior', 34)")

	conn.commit()

create_table()
delete_row()
data_entry()