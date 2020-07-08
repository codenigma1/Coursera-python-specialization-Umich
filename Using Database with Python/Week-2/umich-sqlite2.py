import sqlite3

conn = sqlite3.connect('email.db')
cur = conn.cursor()

def drop_table():
	cur.execute("DROP TABLE IF EXISTS sample")

drop_table()

def create_table():
	cur.execute("CREATE TABLE IF NOT EXISTS sample(email text, count int)")

create_table()

fname = input("Enter the file name: ")
fh = open(fname)

for line in fh:
	if line.startswith("From: "):
		email = line.split(' ')
		data = email[1].strip()
		cur.execute("SELECT count from sample WHERE email = ?", (data,))
		row = cur.fetchone()
		if row is None:
			cur.execute("INSERT INTO sample (email, count) VALUES (?, 1)", (data,))
		else:
			cur.execute("UPDATE sample SET count = count + 1 where email = ?", (data,))

	conn.commit()

sql = "SELECT * FROM sample ORDER BY count DESC LIMIT 10"

for row in cur.execute(sql):
	print(row)


cur.close()
conn.close()





