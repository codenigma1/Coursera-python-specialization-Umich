#! python3
# http://py4e-data.dr-chuck.net/comments_42.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore the ssl certificate errors #
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags #
sum = 0
tags = soup('span')
for tag in tags:
	word = tag.contents[0]
	num = int(word)
	sum = sum + num
print ('The sum is:', sum)	

# Sample code of HTML retrive the informations 

# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
#	  counts = tree.findall('.//count')
