name =  raw_input("Enter the file: ")
fhand = open(name)

dic = dict()
for word in fhand:
    if not word.startswith("From:"):continue
    word = word.split()
    word = word[1]
    dic[word] = dic.get(word, 0) +1

bigcount = None
bigword = None
for k,v in dic.items():
    if bigcount == None or v > bigcount:
        bigword = k 
        bigcount = v 

print bigword, bigcount

# dic = dict()
# for word in fhand :
# 	if word == "": continue
# 	word = word.strip()
# 	if word.startswith("From: "): continue
# 	lst = word.split()
# 	dic[lst = dic.get(lst, 0) + 1

# biggy = None
# Piggy = None
# for k, v in dic.items():
# 	if biggy is None or v > biggy:
# 		biggy = k
# 		Piggy = v
# print biggy, Piggy


# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)



# senders = dict()
# for line in handle:
#     if not line.startswith("From:"):continue
#     line = line.split()
#     line = line[1]
#     senders[line] = senders.get(line, 0) +1
# bigcount = None
# bigword = None
# for word,sender in senders.items():
#     if bigcount == None or sender > bigcount:
#         bigword = word 
#         bigcount = sender 

# print bigword, bigcount