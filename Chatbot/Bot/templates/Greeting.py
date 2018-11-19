import json
from pprint import pprint

myName=input()
with open('D:\\Python\\Django\\DjangoProject\\Chatbot\\Bot\\Greetings.json', 'r') as db:
  greet = json.load(db)
  print(greet[myName])
#myName=input()
#data = json.loads('D:\\Python\\Django\\DjangoProject\\Chatbot\\Bot\\Greetings.json')
#newdata = data.json
#pprint(newdata)