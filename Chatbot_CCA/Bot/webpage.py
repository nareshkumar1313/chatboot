import requests
from requests_ntlm import HttpNtlmAuth
import json
import pprint
import xmltodict
response=requests.get("https://ch1hub.cognizant.com/sites/SC4593/CttWorkSpace/_Vti_bin/listdata.svc/CCAReport?$top=1", auth=HttpNtlmAuth('cts\\265880','Deepu@123'),)
headers ={"accept":"application/json;odata=verbose"}
#pp = pprint.PrettyPrinter(indent=4)

#y= pp.pprint(json.dumps(xmltodict.parse(response.text)))

y=json.dumps(xmltodict.parse(response.text))


json_obj = y[0]['feed'][0]['entry'][0]['content']
print(json_obj)


for i in json_obj:
        key = i['d:AssociateName']
        value = i['d:AssociateID']
        print(key)



