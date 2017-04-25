#import urllib.request
#from bs4 import BeautifulSoup
#import re
import requests
#import json


app_id = '8745a4c9'
app_key = '86e26855b5f985feb88c6cf4b81c4335'
url ='https://od-api.oxforddictionaries.com:443/api/v1/entries/en/'
def search(word, need_examples):    
    
    meanings=''
    url2 =  url + word.lower()
    
    r = requests.get(url2, headers = {'app_id': app_id, 'app_key': app_key})

    #print("code {}\n".format(r.status_code))
 
    #print("json \n" + json.dumps(r.json()))
   
    #print('Meanings \n' + meaningsjson['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])
    if(r.status_code==200):
        counter=0
        meaningsjson=r.json()
        for val in meaningsjson['results'][0]['lexicalEntries']:
            for val2 in val['entries'][0]['senses']:
                counter+=1
                lexical_category=val['lexicalCategory']
                meanings+=str(counter) + ': (' + lexical_category +')' + val2['definitions'][0] + '\n'
                if need_examples == True:
                    examples_count=0
                    if len(val2['examples'])>1:
                        for examples in val2['examples']:
                            examples_count+=1    
                            meanings+='Example ' + str(examples_count) + ": " + examples['text'] + '\n'
                    else:
                        meanings+='Example: ' + examples['text'] + '\n'
                if 'subsenses' in val2.keys():
                    for subsenses_definitions in val2['subsenses']:
                        counter+=1
                        meanings+=str(counter) + ': (' + lexical_category +')' + subsenses_definitions['definitions'][0] + '\n'
                        if need_examples == True:
                            examples_count1=0
                            if len(subsenses_definitions['examples'])>1:
                                for examples_subsenses in subsenses_definitions['examples']:
                                    examples_count1+=1    
                                    meanings+='Example ' + str(examples_count1) + ': ' + examples_subsenses['text'] + '\n'
                            else:
                                meanings+='Example: ' + subsenses_definitions['examples'][0]['text'] + '\n'    
    elif r.status_code==404:
        meanings='Sorry, Word not found' + '\n'
    
    else:
        meanings='Sorry, An error occurred while processing the data' + '\n'
    print(meanings)    
    return(word.upper() + '\n \n' +meanings+'---------------------------------------------------- \n')  

def thesaurus(word, need_examples):
    url2 = url + word + '/synonyms'
    synonyms=''
    r = requests.get(url2, headers = {'app_id': app_id, 'app_key': app_key})
    if r.status_code==200:
        synonymsjson=r.json()
        #print(synonymsjson)
        counter=0
        for val in synonymsjson['results'][0]['lexicalEntries']:
            
            #print(val)
            for val2 in val['entries'][0]['senses']:
                counter+=1
                sense='Sense ' + str(counter)+ '(' + val['lexicalCategory'] +'): \n'
                exampleno=0
                if need_examples == True:
                    if len(val2[lexicalCategory])>1:
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
    elif r.status_code==404:
        synonyms='Sorry, Word not found' + '\n' 
    else:
        synonyms='Sorry, An error occurred while processing the data' + '\n'  
            
    print(synonyms)    
    return(word.upper() + '\n \n' +synonyms+'---------------------------------------------------- \n')
    
#search('ACE', True)

thesaurus('ACE', True)   

  
    
    
    
    