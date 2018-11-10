#! python3

import json
# The most of important think of this program "syntax in data variable". we must follow exact format you cannot use single quote instead of double quote.
data = '''
{
	"name" : "Vaibhav",
	"phone" : {
		"type" : "int1",
		"number" : "9096989201"
	},
	"email" : {
		"hide" : "yes"
	} 
}'''

info = json.loads(data)
print ('Name: ', info['name'])
print ('Email: ', info['email']['hide'])
print ('Phone No: ', info['phone']['number'])