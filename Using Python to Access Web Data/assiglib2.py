#! python3
# Very hard assignement in this course

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore the ssl certificate errors #
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# coun=input('Enter your count:')
# pos=input('Enter your position:')
# print(url)

# for i in range(int(coun)):
# 	html = urllib.request.urlopen(url).read()
# 	soup = BeautifulSoup(html,"html.parser")
# 	tags = soup('a')
# 	url = tags[int(pos)-1].get('href',None)
# print (url)

url = input('Enter the URL: ')
co = input('Enter the count: ')
p = input('Enter the position: ')

for c in range(int(co)):
	html = urllib.request.urlopen(url, context = ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	url = tags[int(p) - 1].get('href', None)
print (url)
	
			
