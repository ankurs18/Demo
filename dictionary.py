import urllib.request
from bs4 import BeautifulSoup
import re

"""html = urllib.request.urlopen("https://www.merriam-webster.com/dictionary/armada")
                 
for var in html: 
    print(var)"""
    
with urllib.request.urlopen('https://www.merriam-webster.com/dictionary/new') as response:
    content = response.read()    

"""data = str(html).split('\\n')   
for var in data:
    print(var)   """


soup = BeautifulSoup(content)#.prettify().encode("utf-8")
"""for tag in soup.find_all('ol'): 
    print(tag.get('class'))"""
    
tag=soup.find('ol')  
for var in tag: 
    defi=str(var)
    i=defi.find('</span>')
    j = defi.rfind('</span>')
    print(i, j)
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
    print(newdef)
    
    
    
    
    
    
    