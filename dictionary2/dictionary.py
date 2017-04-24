#import urllib.request
#from bs4 import BeautifulSoup
#import re
import requests
#import json


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
        #print(synonymsjson)
        counter=0
        for val in synonymsjson['results'][0]['lexicalEntries']:
            sense1=''
            #print(val)
            for val2 in val['entries'][0]['senses']:
                counter+=1
                sense='Sense ' + str(counter)+': \n'
                exampleno=0
                if len(val2['examples'])>1:
                    for example in val2['examples']:
                        exampleno+=1
                        sense +='Example ' + str(exampleno) + ': ' + example['text'] + '\n'
                else:
                    sense+='Example: '+ val2['examples'][0]['text'] + '\n'
                if 'subsenses' in val2.keys():
                    for subsenses in val2['subsenses']:
                        for synonyms_subsenses in subsenses["synonyms"]:
                            sense+=str(synonyms_subsenses['text'])+ ', '
                for synonyms_senses in val2['synonyms']:
                    sense+=str(synonyms_senses['text'])+', '
                sense=sense[:-2]    
                synonyms+=sense+ '\n'                                  
    else:
        synonyms='Sorry, Word not found' + '\n'  
            
    print(synonyms)
    return synonyms
    
thesaurus('ace')   

  
    
    
    
    