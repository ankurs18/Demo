import zipfile, os

print(os.getcwd())
os.chdir('src')
print(os.getcwd())

dirlist = os.listdir('.')
for file in dirlist:
    print(file)
#-----------------    
myzip = zipfile.ZipFile('../myzip.zip', 'w')    
for file in dirlist:
    myzip.write(file)
myzip.close()    

#-----------------
print(myzip.namelist())  
#-----------------
os.chdir('..')

extract = zipfile.ZipFile('myzip.zip')
extract.extractall('dest')
extract.close()
#-----------------

extract = zipfile.ZipFile('myzip.zip')
extract.extract('f1.txt', '.')