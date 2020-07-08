from matplotlib import pyplot as plt
import sqlite3

plt.style.use("fivethirtyeight")

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

def graph_data():
	emails = []
	freq = []
	cur.execute("SELECT * FROM sample ORDER BY count DESC LIMIT 10")
	for row in cur.fetchall():
		emails.append(row[0])
		freq.append(row[1])

	emails.reverse()
	freq.reverse()

	plt.barh(emails, freq)

	plt.title("Most frequent email data from University of Michigan")

	plt.xlabel("Frquency of emails")

	plt.tight_layout()

	plt.show()



graph_data()

cur.close()
conn.close()





