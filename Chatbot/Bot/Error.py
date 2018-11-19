import requests
import json
from django.shortcuts import HttpResponse
from pprint import pprint
from pycorenlp.corenlp import StanfordCoreNLP
from datetime import datetime, timedelta
import pickle
import psycopg2
import psycopg2.extensions
import dicttoxml
import psycopg2
import psycopg2.extensions

listkeys = []
listvalues=[]


host = "http://localhost"
port = "9000"
nlp = StanfordCoreNLP(host + ":" + port)
text = "Show me the flights on May 25 with 1 person from Chicago to Dallas"

nlptext = [nlp.annotate(
        text,
        properties={
                "outputFormat": "json",
                "annotators": "ner,regexner,depparse"
                }
        )]

json_obj = nlptext[0]['sentences'][0]['entitymentions']
city = 0
SOURCE = ''
DESTINATION = ''
d={}
for i in json_obj:
        key = i['ner']
        value = i['text']
        if key== 'DATE':
            key = i['ner']
            value = i['normalizedNER']

            if 'XXXX' in value:
                value = value.replace('XXXX','2018')
                d.update({key:value})
        elif key == 'CITY':
            city+=1
            if(city==1):
                SOURCE = key
                d.update({'SOURCE':value})
            else:
                DESTINATION = key
                d.update({'DESTINATION':value})
        else:
            d.update({key:value})

OriginalList = ['SOURCE','DESTINATION','DATE','NUMBER']
print(OriginalList)


for k in d.keys():
    listkeys.append(k)
print(listkeys)


for k in d.values():
    listvalues.append(k)
print(listvalues)

#missinglist =  (set(listkeys).difference(OriginalList))
missinglist =  (set(OriginalList).difference(listkeys))
print(missinglist)
print("Missing values in second list:", (set(OriginalList).difference(listkeys)))
print(len(missinglist))
mandatoryString = 'Please enter '

if(len(missinglist)>0):
        for i in missinglist:
            if(len(missinglist)==1):
                mandatoryString= mandatoryString + i
            else:
                mandatoryString = mandatoryString + i + ','
        mandatoryString = mandatoryString.replace('SOURCE','Source City')
        mandatoryString = mandatoryString.replace('DESTINATION','Destination City')
        mandatoryString = mandatoryString.replace('DATE','Travel Date')
        mandatoryString = mandatoryString.replace('NUMBER','Passengers Count')
        print(mandatoryString)


        #return HttpResponse(mandatoryString)
elif(OriginalList!=listkeys):
    print('Please enter the details in Sequence of Source,Destination,Date and Passenger Count format')

         #return HttpResponse('Please enter the details in Sequence of Source,Destination,Date and Passenger Count format')

