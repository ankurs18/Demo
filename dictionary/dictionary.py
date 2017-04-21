import urllib.request
from bs4 import BeautifulSoup
<<<<<<< HEAD
=======

>>>>>>> origin/master
import re

"""html = urllib.request.urlopen("https://www.merriam-webster.com/dictionary/armada")
                 
for var in html: 
    print(var)"""


def search(word):    
    with urllib.request.urlopen('https://www.merriam-webster.com/dictionary/'+word) as response:
        content = response.read()    
    
    """data = str(html).split('\\n')   
    for var in data:
        print(var)   """
    
    meanings=''
    soup = BeautifulSoup(content)#.prettify().encode("utf-8")
    """for tag in soup.find_all('ol'): 
        print(tag.get('class'))"""
    if(soup.find_all(name='p', text="The word you've entered isn't in the dictionary. Click on a spelling suggestion below or try again using the search bar above.")):
        meanings="Word not found/n"
    else:
        tag=soup.find('ol')    
        counter=1  
        for var in tag: 
            defi=str(var)
            i=defi.find('</span>')
            j = defi.rfind('</span>')
            #print(i, j)
            defi=defi[i+7:j]
            defi=defi.strip() 
            defi=defi.replace('<em class="vi">', 'EXAMPLE:')
            defi=defi.replace('  ', ' ')
            count1=defi.count('EXAMPLE:')
            k=0
            
            for k in range(count1):
                #print(str(k+1))
                #defi=re.sub('EXAMPLE:', 'EXAMPLE '+str(k)+':', defi)
                #re.purge()
                defi=defi.replace('EXAMPLE:', 'EXAMPLE '+str(k+1)+':',1)
                
            newdef=re.sub('<.*?>','', defi)  
            newdef=re.sub('\s\s',' ', newdef)
            meanings+= str(counter) + ': ' + newdef  + '\n'
            '''.capitalize()'''
            counter+=1
    return(word.upper() + '\n \n' +meanings+'---------------------------------------------------- \n')
<<<<<<< HEAD
    
=======

seachfunc=search    
>>>>>>> origin/master
    
    
    
    