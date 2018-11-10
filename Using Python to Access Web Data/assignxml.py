#! python3
# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_56226.xml
# Simply compute xml data and get sum

import xml.etree.ElementTree as ET
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

tags = soup('count')
sum = 0
for tag in tags:
	counts = int(tag.contents[0])
	sum = sum + counts
print (sum)


# tree = ET.fromstring(soup)
# # data = tree.findall('.//count')
# print (data)










# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     url = serviceurl + urllib.parse.urlencode({'address': address})
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text

#     print('lat', lat, 'lng', lng)
#     print(location)