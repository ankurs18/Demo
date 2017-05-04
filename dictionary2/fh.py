import os
from dictionary import *


def readwrite(path, isDict, isSynonyms):
    print(path)
    objfile=open(path, 'r')
    print(os.curdir)
    mylist=objfile.readlines()
    meanings=''
    
    for var in mylist:
        word=str(var).replace('\n','')
        meanings+=word.upper()+'\n'
        if(isDict):
            meanings+='\n Meanings:\n'+search(word, True)
        if(isSynonyms):
            meanings+='\n Synonyms:\n'+thesaurus(word, True)
        meanings+='---------------------------------------------------- \n'
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