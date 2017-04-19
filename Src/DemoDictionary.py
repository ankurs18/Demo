mydict={101:'Max', 102:'Ankur', 'c101':'ass', 'red':22}
print(mydict)
mydict.update({104:'ada'})
print(mydict)

for key in mydict:
    print(key, mydict.get(key))


for val in mydict.values():
    print(val, end=" ")
    
for key, val in mydict.items():        
    print(key, val)