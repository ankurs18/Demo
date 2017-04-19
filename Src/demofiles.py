import os
import DemoDictionary

#os.makedirs("myfolder")

print(os.path.abspath(".\\myfolder"))
print(os.path.getsize('C:\\jba\\workspaces\\default\\Demo\\Src\\DemoDictionary.py'))
dlist=os.listdir('C:\\jba\\workspaces\\default\\Demo\\Src')

for val in dlist:
    print(val)
    
print(os.path.isdir('C:\\jba\\workspaces\\default\\Demo\\Src'))
print(os.path.isfile('C:\\jba\\workspaces\\default\\Demo\\Src'))

#os.unlink('C:\\myfolder\\as.txt')
os.rmdir('C:\\myfolder')