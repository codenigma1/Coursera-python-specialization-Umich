# Retrieving lists of keys and values #
jjj = {"mad" : 12, "sad" : 34, "cow" : 68}
print list(jjj)
print jjj.keys()
print jjj.values()
print jjj.items()

# Two iteration variable#
mmm = {"dog" : 34, "shot" : 98, "fuck" : 89}
for aaa,bbb in mmm.items() :
	print aaa,bbb
	