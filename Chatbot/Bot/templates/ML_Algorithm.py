import requests
from pycorenlp.corenlp import StanfordCoreNLP
from datetime import datetime, timedelta
import xml
#import Json2xml
import psycopg2
from pprint import pprint
import pickle
listkeys = []
listvalues=[]

host = "http://localhost"
port = "9000"
nlp = StanfordCoreNLP(host + ":" + port)

text = "Show flights from Phoenix to Dallas coming Friday"




nlptext = [nlp.annotate(
text,
    properties={
        "outputFormat": "json",
        "annotators": "ner,regexner,depparse"
    }
    )]

pprint(nlptext)


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
            #key = i['normalizedNER']
            #value = i['ner']
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


for k in d.keys():
    listkeys.append(k)
    if k=='SOURCE':
     listvalues.insert(0, d.get(k))
    if k=='DESTINATION':
     listvalues.insert(1, d.get(k))
    if k=='DATE':
     listvalues.insert(2, d.get(k))
    if k=='NUMBER':
     listvalues.insert(3, d.get(k))
print(listkeys)
print(listvalues)




missinglist =  (set(OriginalList).difference(listkeys))
print("Missing values in second list:", (set(OriginalList).difference(listkeys)))
print(missinglist)
print(len(missinglist))
mandatoryString = 'Please enter '

if(len(missinglist)>0):
        for i in missinglist:
            if(len(missinglist)==1):
                mandatoryString= mandatoryString + i
            else:
                mandatoryString = mandatoryString + i + ','
        mandatoryString = mandatoryString.replace('SOURCE','Source City')
        mandatoryString = mandatoryString.replace('DESTINATION',' Destination City')
        mandatoryString = mandatoryString.replace('DATE',' Travel Date')
        mandatoryString = mandatoryString.replace('NUMBER',' Passengers Count')

        print(mandatoryString)
#elif(OriginalList!=listkeys):
        #listkeys.clear()
        #listvalues.clear()
        #print('Please enter the details in Sequence of Source, Destination, Date and Passenger Count format')




released={
        "Las Vegas"    :"LAS",
        "San Francisco":"SFO",
        "Los Angeles"  :"LAX",
        "Phoenix"     :"PHX",
        "Miami"       :"MIA",
        "Atlanta"     : "ATL",
        "New York"     : "JFK",
        "Seattle"     : "SEA",
        "Dallas"      : "DFW",
        "Chicago"     : "ORD"
    }



if(len(missinglist)==0):
    SOURCE = str(released.get(listvalues[0]))
    DESTINATION = str(released.get((listvalues[1])))
    TRAVELDATE = listvalues[2]
    date = datetime.strptime(TRAVELDATE, "%Y-%m-%d")
    modified_date = date + timedelta(days=1)
    RETURNDATE=datetime.strftime(modified_date, "%Y-%m-%d")
    PASSENGERS = listvalues[3]


print(SOURCE)
print(DESTINATION)
print(TRAVELDATE)
print(RETURNDATE)
print(PASSENGERS)