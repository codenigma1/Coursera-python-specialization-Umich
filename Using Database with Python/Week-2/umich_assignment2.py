import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
c = conn.cursor()

def drop_table():
	c.execute("DROP TABLE IF EXISTS Counts")

drop_table()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS Counts(org TEXT, count INTEGER)")

create_table()


fname = input("Enter the file name: ")
fh = open(fname)

for line in fh:
	if not line.startswith('From: '): continue
	piece = line.split('@')
	orgnaization = piece[1]
	# print(orgnaization)

	c.execute("SELECT count FROM Counts WHERE org = ?", (orgnaization,))
	row = c.fetchone()
	if row is None:
		c.execute("INSERT INTO Counts(org, count) VALUES (?, 1)", (orgnaization,))
	else:
		c.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (orgnaization,))

conn.commit()

sqlstr = "SELECT * FROM Counts ORDER BY count DESC LIMIT 10"


for row in c.execute(sqlstr):
	print(row)
c.close()