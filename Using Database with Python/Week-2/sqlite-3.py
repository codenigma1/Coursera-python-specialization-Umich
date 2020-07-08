import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('umich.db')
c = conn.cursor()


def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS students(unix real, datestampe text, keyword text, value real)")



def data_entry():
	c.execute("INSERT INTO students VALUES(11231233, '2012-06-05', 'Python', 5)")
	conn.commit()
	c.close()
	conn.close()


def dynamic_data_entry():
	unix = time.time()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'Python'
	value = random.randrange(1, 10)
	c.execute("INSERT INTO students(unix, datestampe, keyword, value) VALUES (?, ?, ?, ?)", (unix,date,keyword,value))

	conn.commit()

def read_from():
	c.execute("SELECT * FROM students WHERE value = 6.0")
	for row in c.fetchall():
		print(row)


create_table()
# data_entry()

# for i in range(10):
# 	dynamic_data_entry()
# 	time.sleep(1)

read_from()

c.close()
conn.close()