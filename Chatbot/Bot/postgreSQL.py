import psycopg2
import psycopg2.extensions
import dicttoxml
import json
import requests
import re


#url = "https://api-crt.cert.havail.sabre.com/v1/shop/flights?origin=JFK&destination=LAX&departuredate=2018-07-07&returndate=2018-07-09&onlineitinerariesonly=N&limit=10&offset=1&eticketsonly=N&sortby=totalfare&order=asc&sortby2=departuretime&order2=asc&pointofsalecountry=US"
#headers = {"Authorization": "Bearer T1RLAQK1NoW5E/7639cyZlJVqB1+VVLLeBBOuMtvgidhNUgu1EOjSslDAADAik4NF96No8/rFsqj7bNMaKO7Mywklqp/Zt52v3+5FwP1Pmq2LDFWACjncThjtTsfiQ0xV3/wGnxUwAC8iFn5TrWEuosoLRUW3RVwaB7YpuzWsPaGGApfzEL5ZCxJ4w0XCdcYjCV8gS6pePOkv+CU47rJB0EY9faFknNFdJnWCzyL+3JLY0Io40DvlBBme/J3Ht21KT+gslNtdgowkxXGkv6s0ftj9l8w8ht9QHFOeyNEh8FJtVID7Nam1RAqBcbG"}
#response = requests.get(url,headers)
#AirSearch = response.json()
#xml = dicttoxml.dicttoxml(AirSearch)
#print(xml)
#SOURCE='PHX'
#DESTINATION='LAX'
#TRAVELDATE='2018-05-22'
#PASSENGERS = '1'


#conn = psycopg2.connect("dbname=TravelBot user=postgres password=Database!12")
#cur = conn.cursor()
#insert_query ="INSERT INTO messages (id,createdate,source,destination,traveldate,passenger_ct) VALUES (random()*(255-5)+5,current_date,'"+SOURCE+"','"+DESTINATION+"','"+TRAVELDATE+"','"+PASSENGERS+"')"
#insert_query ="INSERT INTO messages (source,destination,traveldate,passenger_ct) VALUES (?,?,?,?)"
#data = (SOURCE1,DESTINATION1,TRAVELDATE1,PASSENGERS1)
#cur.execute('INSERT INTO messages (id,createdate,source,destination,traveldate,passenger_ct) VALUES (2,current_date,SOURCE1,DESTINATION1,TRAVELDATE1,PASSENGERS1)')
#insert_query="INSERT INTO flight_details (flights_id,flights_res,msg_id)VALUES(random(),'25',1)"
#insert_query= "UPDATE hotel_details SET hotel_id = '1' WHERE msg_id = '1'";
#insert_query="select * from messages"
#print(insert_query)
#cur.execute(insert_query)
#result = cur.fetchall()
#print(result)
#conn.commit()

#xml = '','1'


conn = psycopg2.connect("dbname=TravelBot user=postgres password=Database!12")
cur = conn.cursor()
insert_query = "select  max(id) from messages"
maxid =cur.execute(insert_query)
result= cur.fetchone()
print(result[0])
conn.commit()


