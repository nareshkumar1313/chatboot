from pprint import pprint
from pycorenlp.corenlp import StanfordCoreNLP
from datetime import datetime, timedelta
    

host = "http://localhost"
port = "9000"
nlp = StanfordCoreNLP(host + ":" + port)
    
text = "I want to travel from Las Vegas to Dallas on 25 MAY with"
    
nlptext = [nlp.annotate(
        text,
        properties={
                "outputFormat": "json",
                "annotators": "ner,regexner,depparse"
                }
        )]
    
#pprint(nlptext)


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
listkeys = [ k for k in d.keys() ]
listvalues = [ k for k in d.values() ]

#print("original list is:", OriginalList)
#print("Keys list is:", listkeys)
#print("Values list is:", listvalues)

missinglist =  (set(OriginalList).difference(listkeys))
#print("Missing values in second list:", (set(OriginalList).difference(listkeys)))
#print(len(missinglist))

for i in missinglist:
    if i=='SOURCE':
        print('Please enter Source City')
        #return HttpResponse('Please enter Source City')
    elif i=='DESTINATION':
        print('Please enter Destination City')
        #return HttpResponse('Please enter Destination City')
    elif i=='DATE':
        print('Please enter Departure Date')
        #return HttpResponse('Please enter Departure Date')
    elif i=='NUMBER':
        print('Please enter Passengers count')
        #return HttpResponse('Please enter Passengers count')

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
    DESTINATION = str(released.get(listvalues[1]))
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







#newlist = []

#print(newlist)


