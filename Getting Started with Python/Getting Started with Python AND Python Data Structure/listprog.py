ope = open("open_command.txt")
for f in ope : 
	fu = f.rstrip()
	if not fu.startswith("from:") :
		continue
	line = fu.split()
	print line[2] 	


