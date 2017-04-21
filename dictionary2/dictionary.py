import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import json


app_id = '8745a4c9'
app_key = '86e26855b5f985feb88c6cf4b81c4335'

def search(word):    
    
    meanings=''
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + 'en' + '/' + word.lower()
    
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

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
        meanings='Sorry, Word not found' 
        
    return(word.upper() + '\n \n' +meanings+'---------------------------------------------------- \n')  
search('armada')    

  
    
    
    
    