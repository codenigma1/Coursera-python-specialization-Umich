import sqlite3

conn = sqlite3.connect('umich.db')
c = conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS students(ID int, fname text, language text)')


def data_entry():
	c.execute("INSERT INTO students VALUES(2, 'Arshad', 'R, Python'), (3, 'Prashik', 'STATA')")
	conn.commit()
	c.close()
	conn.close()


create_table()
data_entry()