#! python3

import xml.etree.ElementTree as ET

data = '''
<person>
	<name>Vaibhav</name>
	<phone type = "int1">
		9096989201
	</phone>
	<email hide = "yes"/>
</person>'''
			
tree = ET.fromstring(data)
print ('Name: ', tree.find('name').text)
print ('Attr: ', tree.find('email').get('hide'))
print ('Phone no: ', tree.find('phone').get('type'))			
