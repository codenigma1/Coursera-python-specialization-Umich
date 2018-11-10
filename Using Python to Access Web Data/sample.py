#! python3

import json

data = '''{
	"name" : "Mahendra",

	"phone" : {
		"type" : "landline",
		"country_code" : "+91",
		"number" : "9096989201"
	},

	"email" : "khobragade.vaibhav8@gmail.com"
}'''

info = json.loads(data)
for i in info:

	print("Name: ", i["name"])
	print("Phone No.: ", i["country_code"]["number"])
	print("Email id: ", i["email"])