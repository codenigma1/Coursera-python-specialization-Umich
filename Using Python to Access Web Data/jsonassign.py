#! python3
#Simply decode JSON data and compute sum

import urllib.request, urllib.parse, urllib.error
import json

url = input ('Enter the url: ')
web = urllib.request.urlopen(url)
data = web.read().decode()
tree = json.loads(data)
d = tree['comments']
sum = 0
for line in d:
	val = line['count']
	sum = sum + val
print (sum)	