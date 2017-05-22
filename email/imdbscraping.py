import urllib.request
from bs4 import BeautifulSoup
import re

def search(show):
    
    url = 'http://epguides.com/' + str(show).replace(' ', '')
    with urllib.request.urlopen(url) as response:
        content = response.read()   
        
    data = ''
    soup = BeautifulSoup(content)
    tag = soup.find('pre')   
    #print(tag)
    list = []
    flag = 0
    for var in tag: 
        if flag == 1:
            if 'href' not in str(var) and str(var).count('\n') < 3:
                if '    ' in str(var):
                    var=str(var)[str(var).find('    ')+4:]
                   
                list.append(var[0:-3]) 
        if str(var).find('<a id="latest"></a>')>-1:
            flag = 1
    
    
    
    elist = []  
    for val in list:
        dictionary = {}
        #print(val)
        #print('------------')
        i=str(val).count(' ')
        
        dictionary['Episode'] = str(val)[0:val.find(' ')]
        dictionary['Date'] = str(val)[i:] 
        elist.append(dictionary)
        
    print(elist)
    
search('silicon valley')    
    