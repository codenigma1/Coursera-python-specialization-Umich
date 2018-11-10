#! python3

import json

data = '''
[
	{
	"id" : "001",
	"x" : "1",
	"name" : "Mahindra",
	"sex" : "Male"
	},
	{
	"id" : "002",
	"x" : "2",
	"name" : "Sumit Temburne",
	"sex" : "Transgender"
	}
]'''

info = json.loads(data)
print ('User count:', len(info))

for line in info:	
	print ('Name:', line['name'])
	print ('Sex :', line['sex'])
	print ('id: ', line['id'])
	print ('Attrib: ', line['x'])	
