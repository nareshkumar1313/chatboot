import requests
import json
from django.shortcuts import HttpResponse#pip install django
from pprint import pprint
from pycorenlp.corenlp import StanfordCoreNLP#pip install pycorenlp
from datetime import datetime, timedelta
import pickle
import psycopg2#easy_install psycopg2
import psycopg2.extensions
import dicttoxml# pip install dicttoxml



listkeys = []
listvalues=[]

def get_flightresults(request, question_id):
    print(question_id)
    text=question_id

    Greetings = ['hi','hello','good morning','good evening','hey','bye','good bye','wassup']
    #if not 'search' in question_id:
    if text.lower() in Greetings:
        with open('D:\\Python\\Django\\DjangoProject\\Chatbot\\Bot\\Greetings.json', 'r') as db:
            greet = json.load(db)
            question_id = question_id.lower()
            print(greet[question_id])
            return HttpResponse(greet[question_id])
    else:
        host = "http://localhost"
        port = "9000"
        nlp = StanfordCoreNLP(host + ":" + port)

    #text = "I want to travel from Las Vegas to Dallas on 25 MARCH with 3 persons"

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

        return HttpResponse(mandatoryString)
    #elif(OriginalList!=listkeys):
         #listkeys.clear()
         #listvalues.clear()
         #return HttpResponse('Please enter the details in Sequence of Source, Destination, Date and Passenger Count format')




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

        try:
            conn = psycopg2.connect("dbname=TravelBot user=postgres password=Database!12")
            cur = conn.cursor()
            insert_query ="INSERT INTO messages (createdate,source,destination,traveldate,passenger_ct) VALUES (current_date,'"+SOURCE+"','"+DESTINATION+"','"+TRAVELDATE+"','"+PASSENGERS+"')"
            cur.execute(insert_query)
            conn.commit()
            print("DB Updated Successfully")
        except (psycopg2.Error, psycopg2.Warning) as e:
            print(e)
        finally:
            conn.close()

        url = "https://api.test.sabre.com/v1/shop/flights?origin="+SOURCE+"&destination="+DESTINATION+"&departuredate="+TRAVELDATE+"&returndate="+RETURNDATE+"&onlineitinerariesonly=N&limit=40&offset=1&sortby=totalfare&passengercount="+PASSENGERS+"&order=asc&sortby2=departuretime&order2=asc"
        headers = {"Authorization": "Bearer T1RLAQLCjB2CkR2jWYRVKhUYy4pRwHoXNBDSsSwz6L4p47FL8eUFLsrTAADAbiqjyZxAI3KQ0oh+S8NO0JWtyQfJ5WbJQQn+6y3gKyqqermBzG7eOg4xN6QRUHRBKrWtuJtaQv9mUpCyo7Nth9p9H7iHatNTwrNlIovwGF3D9PysgN4bXsNUZfTsNM7FUMRCBBNvchT6ZsVSJ2yIHXQGKwfegRmL+T4A1aX619xlm9IHP6L0Bj2WhfVX+ABxeiGqtG5GsEMRIll9oXwf9xUEsbo2Guty+UzGNI+xJ5N9JBzoxkz/YoRZ8wYPP6Gx"}
        response = requests.get(url,headers)
        AirSearch = response.json()
        xml = dicttoxml.dicttoxml(AirSearch).decode('utf-8')
        #print(xml)
        try:
            conn = psycopg2.connect("dbname=TravelBot user=postgres password=Database!12")
            cur = conn.cursor()
            insert_query = "INSERT INTO flight_details (flights_res)VALUES('"+xml+"')"
            cur.execute(insert_query)
            conn.commit()
            print("DB Updated Successfully")
        except (psycopg2.Error, psycopg2.Warning) as e:
            print(e)
        finally:
            conn.close()

        print('\nHere are the Flight details based on your inputs..\n')
        print('Inward')
        #print(AirSearch)

        if 'No results were found' in AirSearch:
            return HttpResponse('Unable to display flights & Hotels')
        else:
            a= (AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['Code'])
            b= (AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])
            timestamp1= (AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['DepartureDateTime'])
            time = timestamp1.split('T')
            tt = time[1].split(':')
            c = tt[0]+':'+tt[1]
            d= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
            e= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['Cabin']['Cabin'])
            f= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['SeatsRemaining']['Number'])
            g=(AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
            h=(AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])

            print(a,b,c,d,e,f,g,h)


            a1= (AirSearch['PricedItineraries'][8]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['Code'])
            b1= (AirSearch['PricedItineraries'][8]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])
            timestamp1= (AirSearch['PricedItineraries'][8]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['DepartureDateTime'])
            time = timestamp1.split('T')
            tt = time[1].split(':')
            c1 = tt[0]+':'+tt[1]
            d1= (AirSearch['PricedItineraries'][8]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
            e1= (AirSearch['PricedItineraries'][8]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['Cabin']['Cabin'])
            f1= (AirSearch['PricedItineraries'][8]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['SeatsRemaining']['Number'])
            g1=(AirSearch['PricedItineraries'][8]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
            h1=(AirSearch['PricedItineraries'][8]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])
            print(a1,b1,c1,d1,e1,f1,g1,h1)

            a2= (AirSearch['PricedItineraries'][15]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['Code'])
            b2= (AirSearch['PricedItineraries'][15]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])

            timestamp1= (AirSearch['PricedItineraries'][15]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['DepartureDateTime'])
            time = timestamp1.split('T')
            tt = time[1].split(':')
            c2 = tt[0]+':'+tt[1]
            d2= (AirSearch['PricedItineraries'][15]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
            e2= (AirSearch['PricedItineraries'][15]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['Cabin']['Cabin'])
            f2= (AirSearch['PricedItineraries'][15]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['SeatsRemaining']['Number'])
            g2=(AirSearch['PricedItineraries'][15]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
            h2=(AirSearch['PricedItineraries'][15]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])
            print(a2,b2,c2,d2,e2,f2,g2,h2)

            x=(AirSearch['PricedItineraries'][0]['AirItinerary']['DirectionInd'])
            print('\n'+x)
            a3= (AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['OperatingAirline']['Code'])
            b3= (AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])
            c3=(AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['DepartureDateTime'])
            d3= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
            e3= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][1]['TPA_Extensions']['Cabin']['Cabin'])
            f3= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][1]['TPA_Extensions']['SeatsRemaining']['Number'])
            g3=(AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
            h3=(AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])

            print(a3,b3,c3,d3,e3,f3,g3,h3)


            a4= (AirSearch['PricedItineraries'][1]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['OperatingAirline']['Code'])
            b4= (AirSearch['PricedItineraries'][1]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])
            c4=(AirSearch['PricedItineraries'][1]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['DepartureDateTime'])
            d4= (AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
            e4= (AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][1]['TPA_Extensions']['Cabin']['Cabin'])
            f4= (AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][1]['TPA_Extensions']['SeatsRemaining']['Number'])
            g4=(AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
            h4=(AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])
            print(a4,b4,c4,d4,e4,f4,g4,h4)

            a5= (AirSearch['PricedItineraries'][2]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['OperatingAirline']['Code'])
            b5= (AirSearch['PricedItineraries'][2]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])
            c5=(AirSearch['PricedItineraries'][2]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][1]['FlightSegment'][0]['DepartureDateTime'])
            d5= (AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
            e5= (AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][1]['TPA_Extensions']['Cabin']['Cabin'])
            f5= (AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][1]['TPA_Extensions']['SeatsRemaining']['Number'])
            g5=(AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
            h5=(AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])
            print(a5,b5,c5,d5,e5,f5,g5,h5)
            hotelresponse = get_hotels(DESTINATION)
            #img=mpimg.imread('D:\\Python\\Django\\DjangoProject\\Chatbot\Bot\\static\\united-airlines.jpg')
            #imgplot = plt.imshow(img)
            listkeys.clear()
            listvalues.clear()
            try:
                conn = psycopg2.connect("dbname=TravelBot user=postgres password=Database!12")
                cur = conn.cursor()
                insert_query = "select  max(id) from messages"
                cur.execute(insert_query)
                maxid= cur.fetchone()
                UniqueID=maxid[0]
                print(UniqueID)
                conn.commit()

            except (psycopg2.Error, psycopg2.Warning) as e:
                print(e)
            finally:
                conn.close()



            return HttpResponse("Here are the Flight details %s " % '<br/>'+'Inward:'+'<br/>'+'<a href="www.google.com">'+str(a)+' '+str(b)+'</a>'+' '+str(c)+' '+str(d)+' '+'Economy'+' '+str(f)+' '+'<br/>'+'<a href="www.google.com">'+str(a1)+' '+str(b1)+'</a>'+' '+str(c1)+' '+str(d1)+' '+'Economy'+' '+str(f1)+' '+'<br/>'+'<a href="www.yahoo.com">'+str(a2)+' '+str(b2)+'</a>'+' '+str(c2)+' '+str(d2)+' '+'Economy'+' '+str(f2)+'<br/>'+str(hotelresponse)+'<br/>'+'<b style="color:blue;">'+"Please use this Unique ID while talking to our Agents-AIRSR100"+str(UniqueID))
            #return HttpResponse("Here are the Flight details based on your inputs.. %s " % '<br/>'+'Inward:'+'<br/>'+'<img src="file:///D://Python//Django//DjangoProject//Chatbot//Bot//static//UnitedAirlines.png" style="height: 30px;>'+' '+str(b)+' '+str(c)+' '+str(d)+' '+'Economy'+' '+str(f)+' '+'<br/>'+'<a href="www.google.com">'+str(a1)+' '+str(b1)+'</a>'+' '+str(c1)+' '+str(d1)+' '+'Economy'+' '+str(f1)+' '+'<br/>'+'<a href="www.yahoo.com">'+str(a2)+' '+str(b2)+'</a>'+' '+str(c2)+' '+str(d2)+' '+'Economy'+' '+str(f2)+'<br/>'+str(hotelresponse))
            #return HttpResponse("Here are the Flight details based on your inputs.. %s " % '<br/>'+'Inward:'+'<br/>'+'<img src="file:///D://Python//Django//DjangoProject//Chatbot//Bot//static//UnitedAirlines.png" style="height: 30px;>'+' '+str(b)+' '+str(c)+' '+str(d)+' '+'Economy'+' '+str(f)+' '+'<br/>'+'<a href="www.google.com">'+str(a1)+' '+str(b1)+'</a>'+' '+str(c1)+' '+str(d1)+' '+'Economy'+' '+str(f1)+' '+'<br/>'+'<a href="www.yahoo.com">'+str(a2)+' '+str(b2)+'</a>'+' '+str(c2)+' '+str(d2)+' '+'Economy'+' '+str(f2)+'<br/>'+str(hotelresponse))


def get_hotels(DESTINATION):
    hotel={
    "LAS":[51308,43885,36422],
    "SFO":[31912,25032,42524],
    "LAX":[46169,20632,14838],
    "PHX":[8699,48536,31106],
    "MIA":[2467,88068,2056],
    "ATL":[49291,9101,112407],
    "JFK":[27119,11181,73652],
    "SEA":[80986,9157,3687],
    "DFW":[44255,51197,21899],
    "ORD":[6841,9107,22535]
}
    NEARHOTELS = hotel.get(DESTINATION)
    url="https://api.test.sabre.com/v1.0.0/shop/hotels/content?mode=content"
    data={
            "GetHotelContentRQ": {
                    "SearchCriteria": {
                            "HotelRefs": {
                                    "HotelRef": [
                                            {
                                                    "HotelCode": str(NEARHOTELS[0])
                                                    },
                                            {
                                                    "HotelCode": str(NEARHOTELS[1])
                                                    },
                                            {
                                                    "HotelCode": str(NEARHOTELS[2])
                                                    }
                                            ]
                                    },
                                    "DescriptiveInfoRef": {
                                            "PropertyInfo": True,
                                            "LocationInfo": True,
                                            "Amenities": True,
                                            "Descriptions": {
                                                    "Description": [{
                                                            "Type": "Dining"
                                                            }, {
                                                                    "Type": "Alerts"
                                                                    }]
                                    },
                                    "Airports": True,
                                    "AcceptedCreditCards": True
                                    },
                                    "ImageRef": {
                                            "MaxImages": "10"
                                            }
                            }
                    }
            }
	
    headers = {'Authorization': 'Bearer T1RLAQLCjB2CkR2jWYRVKhUYy4pRwHoXNBDSsSwz6L4p47FL8eUFLsrTAADAbiqjyZxAI3KQ0oh+S8NO0JWtyQfJ5WbJQQn+6y3gKyqqermBzG7eOg4xN6QRUHRBKrWtuJtaQv9mUpCyo7Nth9p9H7iHatNTwrNlIovwGF3D9PysgN4bXsNUZfTsNM7FUMRCBBNvchT6ZsVSJ2yIHXQGKwfegRmL+T4A1aX619xlm9IHP6L0Bj2WhfVX+ABxeiGqtG5GsEMRIll9oXwf9xUEsbo2Guty+UzGNI+xJ5N9JBzoxkz/YoRZ8wYPP6Gx','Content-Type' : 'application/json'}
    response2 = requests.post(url,headers=headers,data=json.dumps(data))
    HotelSearch = response2.json()
    print(HotelSearch)
    xml = dicttoxml.dicttoxml(HotelSearch).decode('utf-8')
    try:
        conn = psycopg2.connect("dbname=TravelBot user=postgres password=Database!12")
        cur = conn.cursor()
        insert_query = "INSERT INTO hotel_details(hotel_rsp)VALUES('"+xml+"')"
        cur.execute(insert_query)
        conn.commit()
        print("DB Updated Successfully")
    except (psycopg2.Error, psycopg2.Warning) as e:
            print(e)
    finally:
            conn.close()
    if 'No results were found' in HotelSearch:
        return HttpResponse('Unable to display nearby hotels')
    else:
        print('\nNear By Hotels..')
        ah=(HotelSearch['GetHotelContentRS']['HotelContentInfos']['HotelContentInfo'][0]['HotelInfo']['ChainName'])
        ap=(HotelSearch['GetHotelContentRS']['HotelContentInfos']['HotelContentInfo'][0]['HotelDescriptiveInfo']['LocationInfo']['Contact']['Phone'])
        bh=(HotelSearch['GetHotelContentRS']['HotelContentInfos']['HotelContentInfo'][1]['HotelInfo']['ChainName'])
        bp=(HotelSearch['GetHotelContentRS']['HotelContentInfos']['HotelContentInfo'][1]['HotelDescriptiveInfo']['LocationInfo']['Contact']['Phone'])

        ch=(HotelSearch['GetHotelContentRS']['HotelContentInfos']['HotelContentInfo'][2]['HotelInfo']['ChainName'])
        cp=(HotelSearch['GetHotelContentRS']['HotelContentInfos']['HotelContentInfo'][2]['HotelDescriptiveInfo']['LocationInfo']['Contact']['Phone'])


        return "Near By Hotels.. %s" % '<br/>'+str(ah)+'<b>'+' P:'+ap+'</b>'+'<br/>'+str(bh)+'<b>'+' P:'+bp+'</b>'+'<br/>'+str(ch)+'<b>'+' P:'+cp+'</b>'



#for k in listkeys:
 #   listkeys.remove(k)
#for k in listvalues:
 #   listvalues.remove(k)