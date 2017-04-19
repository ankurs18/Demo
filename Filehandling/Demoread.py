#r parameter symbolises read mode
objfile=open('data.txt', 'r')
print(objfile.read())

objfile.seek(0)
print(objfile.read())

objfile.seek(0)
#readlines will give a list of strings
mylist=objfile.readlines()
print(mylist)