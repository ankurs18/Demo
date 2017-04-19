info = '{"name": "Ankur", "ID": 101, "city":"Pune"}'

import json

#returns dictionary(key-value pair)
mydict = json.loads(info)

print(mydict)