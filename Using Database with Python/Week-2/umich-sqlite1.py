import sqlite3

conn = sqlite3.connect('email.db')
c = conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS sample(email text, count int)")

create_table()

fname = input("Enter the file name: ")
fh = open(fname)

for line in fh:
	if not line.startswith('From: '): continue
	piece = line.split('@')
	email = piece[1]
	c.execute("SELECT count FROM sample WHERE email = ?", (email,))
	row = c.fetchone()
	if row is None:
		c.execute("INSERT INTO sample(email, count) VALUES (?, 1)", (email,))
	else:
		c.execute("UPDATE sample SET count = count + 1 WHERE email = ?", (email,))

	conn.commit()

sqlstr = "SELECT * FROM sample ORDER BY count DESC LIMIT 10"

for row in c.execute(sqlstr):
	print(str(row[0], row[1]))


c.close()
conn.close()




