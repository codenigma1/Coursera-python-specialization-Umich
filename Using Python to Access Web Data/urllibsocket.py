#! python3

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://yupmytrick.wordpress.com/2015/04/30/all-airtel-free-internet-3g-trick-may-2015/')
for line in fhand:
	print (line.decode().strip())
	

