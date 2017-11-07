#import json

#pp=pprint.PrettyPrinter(indent=4)
#pp.pprint(mydict)


#parsed = json.loads(rs.json)
#print json.dumps(parsed, indent=4, sort_keys=True)i
import json
from pprint import pprint

with open('rs.json') as data_file:    
    data = json.load(data_file)

pprint(data)
