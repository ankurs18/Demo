import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import json


app_id = '8745a4c9'
app_key = '86e26855b5f985feb88c6cf4b81c4335'
url ='https://od-api.oxforddictionaries.com:443/api/v1/entries/en/'
def search(word):    
    
    meanings=''
    url2 =  url + word.lower()
    
    r = requests.get(url2, headers = {'app_id': app_id, 'app_key': app_key})

    #print("code {}\n".format(r.status_code))
 
    #print("json \n" + json.dumps(r.json()))
   
    #print('Meanings \n' + meaningsjson['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])
    if(r.status_code==200):
        counter=0
        meaningsjson=r.json()
        for val in meaningsjson['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
            counter+=1
            #print('meaning1' + val['definitions'][0])
            meanings+=str(counter) + ': ' + val['definitions'][0] + '\n'
    else:
        meanings='Sorry, Word not found' + '\n'
    print(meanings)    
    return(word.upper() + '\n \n' +meanings+'---------------------------------------------------- \n')  

def thesaurus(word):
    url2 = url + word + '/synonyms'
    synonyms=''
    r = requests.get(url2, headers = {'app_id': app_id, 'app_key': app_key})
    if r.status_code==200:
        synonymsjson=r.json()
        print(synonymsjson)
        counter=0
        for val in synonymsjson['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
            counter+=1
            #print(val)
            synonyms+='Sense ' + str(counter)+': '+ val['examples'][0]['text']+'\n'
            for val2 in val['subsenses'][0]['synonyms']:
                synonyms+=val2['text'] + ', '
            for val3 in val['synonyms']:
                syonyms+=val3['text'] + ', '
            synonyms+='\n'    
                
    else:
        synonyms='Sorry, Word not found' + '\n'  
            
    print(synonyms)
    
thesaurus('new')   

  
    
    
    
    