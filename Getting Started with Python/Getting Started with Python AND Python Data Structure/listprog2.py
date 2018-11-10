# Double split pattern program using split() funtion #
# This is program great understanding of whole list lesson #
ope = open("open_command.txt")
for f1 in ope :
	fu1 = f1.rstrip()
	if not fu1.startswith("from:") :
		continue
	line = fu1.split() # Look carefully clumsy boy #
	email = line[1]
	piece = email.split("@")
	print piece[1]	
