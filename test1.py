import json
f = open('labels_commadelim.csv','r')
arr=[]
headers = []

for header in f.readline().split(','):
	headers.append(header)



for line in f.readlines():
	lineItems = {}
	for i,item in enumerate(line.split(',')):  
		lineItems[headers[i]] = item


arr.append(lineItems)

f.close()

jsonText = json.dumps(arr)

print jsonText
