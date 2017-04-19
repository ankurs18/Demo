import dictionary
import os


def readwrite(path):
    print(path)
    objfile=open(path, 'r')
    print(os.curdir)
    mylist=objfile.readlines()
    meanings=''
    for var in mylist:
        meanings+=dictionary.search(str(var).replace('\n',''))
        #print(str(var).replace('\n',''))
        
    print(meanings)   
    npath=str(path)
    loc=npath.rfind('/')
    writepath=npath[:loc]+'/meanings.txt'
    print(writepath)                                
    writefile=open(writepath, 'w')
    
    
    status=writefile.write(meanings)
    
    objfile.close()
    writefile.close()
    return status