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
            list.append(var) 
        if str(var).find('<a id="latest"></a>')>-1:
            flag = 1
    
    for val in list:
        print(val)
        print('------------')
          
    
    
search('silicon valley')    
    