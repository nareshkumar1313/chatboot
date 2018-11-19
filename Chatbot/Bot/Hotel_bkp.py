from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests
import json
#from django.shortcuts import render, HttpResponse

#-------------------REMOVE STOP WORDS and FILTER/REQUEST/RESPONSE TO API----------------------------------------

def get_flightresults():
        #print(question_id)
        #Sentence=question_id
        #intermediateData = dict(x.POST)
        #print(x)
        Sentence="I want to travel from SFO to LAX on 2018-02-15 with 1 persons in AA"
        stop_words=set(stopwords.words("english"))
        words=word_tokenize(Sentence)
        filtered_sentence=[w for w in words if not w in stop_words]
        words1 = ['I','You','Me','We','travel','book','want','persons']
        result=[w for w in filtered_sentence if not w in words1]
        print(result)
        
        #url = "https://api.test.sabre.com/v1/shop/flights?origin="+result[0]+"&destination="+result[1]+"&departuredate="+result[2]+"&returndate=2018-02-06&onlineitinerariesonly=N&limit=10&offset=1&eticketsonly=N&sortby=totalfare&order=asc&sortby2=departuretime&order2=asc"
        #url = "https://api.test.sabre.com/v1/shop/flights?origin="+result[0]+"&destination="+result[1]+"&departuredate="+result[2]+"&returndate=2018-02-16&onlineitinerariesonly=N&limit=10&offset=1&sortby=totalfare&order=dsc&sortby2=departuretime&passengercount="+result[3]+"&order2=dsc"
        url = "https://api.test.sabre.com/v1/shop/flights?origin="+result[0]+"&destination="+result[1]+"&departuredate="+result[2]+"&returndate=2018-02-06&onlineitinerariesonly=N&limit=10&offset=1&sortby=totalfare&order=dsc&sortby2=departuretime&passengercount="+result[3]+"&includedcarriers="+result[4]+"&order2=asc"
        headers = {"Authorization": "Bearer T1RLAQJDIHE5hYVcOwWOikZAiyddBOG7fhCkVt2w2VXdkFLuwUrw0WcZAADA9k7hHZvUKApuYUbJsrSyUdVJ71tpYuFNw6AkLwJtPz1LVY7UaiEUBwpz/Ezu7ZMZ9DyOKEnIZXnPdnY7YnRTWIpm8LYEXan++3Txjq0YzPpmTEbnY9s5C62tlS8lir9e8i/Jrc58MYVitXPHYDOptlHqGAjUzBv+tfmjz+s33IZZ3E/xpgrh4FFgAB570Mu5sfLkhYYe9xG7xbXDwsK+54H/U2k8m8oCrXySGe2OpbcIdwZGtVYHRLz7Ee7yCQrC"}
        response = requests.get(url,headers)
        AirSearch = response.json()
        
        print('\nHere are the Flight details based on your inputs..\n')
        print('Inward')
        #print(AirSearch)
        #print(len(actualdata['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']))
        a= (AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['Code'])
        b= (AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])
        c= (AirSearch['PricedItineraries'][0]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['DepartureDateTime'])
        d= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
        e= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['Cabin']['Cabin'])
        f= (AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['SeatsRemaining']['Number'])
        
        g=(AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
        h=(AirSearch['PricedItineraries'][0]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])
        
        print(a,b,c,d,e,f,g,h)
                
                
        a1= (AirSearch['PricedItineraries'][1]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['Code'])
        b1= (AirSearch['PricedItineraries'][1]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])
        c1= (AirSearch['PricedItineraries'][1]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['DepartureDateTime'])
        d1= (AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
        e1= (AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['Cabin']['Cabin'])
        f1= (AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['SeatsRemaining']['Number'])
        g1=(AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
        h1=(AirSearch['PricedItineraries'][1]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])
        print(a1,b1,c1,d1,e1,f1,g1,h1)
        
        a2= (AirSearch['PricedItineraries'][2]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['Code'])
        b2= (AirSearch['PricedItineraries'][2]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['OperatingAirline']['FlightNumber'])
        c2= (AirSearch['PricedItineraries'][2]['AirItinerary']['OriginDestinationOptions']['OriginDestinationOption'][0]['FlightSegment'][0]['DepartureDateTime'])
        d2= (AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['Amount'])
        e2= (AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['Cabin']['Cabin'])
        f2= (AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['FareInfos']['FareInfo'][0]['TPA_Extensions']['SeatsRemaining']['Number'])
        g2=(AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Quantity'])
        h2=(AirSearch['PricedItineraries'][2]['AirItineraryPricingInfo']['PTC_FareBreakdowns']['PTC_FareBreakdown']['PassengerTypeQuantity']['Code'])
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

        #return HttpResponse("Here are the Flight details based on your inputs.. %s." % 'Inward'+"\n"+str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(a1)+str(b1)+str(c1)+str(d1)+str(e1)+str(f1)+str(g1)+str(h1)+str(a2)+str(b2)+str(c2)+str(d2)+str(e2)+str(f2)+str(g2)+str(h2)+ str('\n'+x)+"\n"+str(a3)+str(b3)+str(c3)+str(d3)+str(e3)+str(f3)+str(g3)+str(h3)+str(a4)+str(b4)+str(c4)+str(d4)+str(e4)+str(f4)+str(g4)+str(h4))
        #return HttpResponse(str(x))
        #return HttpResponse(str(a3)+str(b3)+str(c3)+str(d3)+str(e3)+str(f3)+str(g3)+str(h3)+str(a4)+str(b4)+str(c4)+str(d4)+str(e4)+str(f4)+str(g4)+str(h4))

        
        url = "https://api.test.sabre.com/v1.0.0/shop/hotels/list?mode=list"
                       
        data={
	"GetHotelListRQ": {
		"SearchCriteria": {
			"IncludedFeatures": True,
			"HotelRefs": {
				"HotelRef": [{
						"HotelCode": "22570"
                        
					},
					{
						"HotelCode": "21587"
					},
					{
						"HotelCode": "5524"
					}
				]
			}
		}
	}
}
                        
        
                     
        headers = {'Authorization': 'Bearer T1RLAQJDIHE5hYVcOwWOikZAiyddBOG7fhCkVt2w2VXdkFLuwUrw0WcZAADA9k7hHZvUKApuYUbJsrSyUdVJ71tpYuFNw6AkLwJtPz1LVY7UaiEUBwpz/Ezu7ZMZ9DyOKEnIZXnPdnY7YnRTWIpm8LYEXan++3Txjq0YzPpmTEbnY9s5C62tlS8lir9e8i/Jrc58MYVitXPHYDOptlHqGAjUzBv+tfmjz+s33IZZ3E/xpgrh4FFgAB570Mu5sfLkhYYe9xG7xbXDwsK+54H/U2k8m8oCrXySGe2OpbcIdwZGtVYHRLz7Ee7yCQrC',
                   'Content-Type' : 'application/json'}
        
        response2 = requests.post(url,headers=headers,data=json.dumps(data))
        HotelSearch = response2.json()
        #print(HotelSearch)
        
        print('\nNear By Hotels..')
        ah= (HotelSearch['GetHotelListRS']['HotelList']['HotelRef'][0]['HotelInfo'][0]['HotelName'])
        bh= (HotelSearch['GetHotelListRS']['HotelList']['HotelRef'][0]['HotelInfo'][1]['HotelName'])
        ch=(HotelSearch['GetHotelListRS']['HotelList']['HotelRef'][0]['HotelInfo'][2]['HotelName'])
        #return HttpResponse("Here are the Flight details based on your inputs.. %s. " % 'Inward'+"\n"+str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '+str(e)+' '+str(f)+' '+str(g)+' '+str(h)+' '+"\n"+str(a1)+' '+str(b1)+' '+str(c1)+' '+str(d1)+' '+str(e1)+' '+str(f1)+' '+str(g1)+' '+str(h1)+' '+'<br/>'+str(a2)+' '+str(b2)+' '+str(c2)+' '+str(d2)+' '+str(e2)+' '+str(f2)+' '+str(g2)+' '+str(h2)+' '+'\n'+str('\n x')+'\n'+str(a3)+' '+str(b3)+' '+str(c3)+' '+str(d3)+' '+str(e3)+' '+str(f3)+' '+str(g3)+' '+str(h3)+' '+'\n'+str(a4)+' '+str(b4)+' '+str(c4)+' '+str(d4)+' '+str(e4)+' '+str(f4)+' '+str(g4)+' '+str(h4)+' '+"\n"+"Near By Hotels.. %s." % '\n'+str(ah)+' '+str(bh)+' '+str(ch))

        #return HttpResponse("Near By Hotels.. %s." % str(ah)+str(bh)+str(ch))
    #print(a,"\n"+b,"\n"+c)
#get_flightresults()
        
        

    

 #{‘ourselves’, ‘hers’, ‘between’, ‘yourself’, ‘but’, ‘again’, ‘there’, ‘about’, ‘once’, ‘during’, ‘out’, ‘very’, ‘having’, ‘with’, ‘they’, ‘own’, ‘an’, ‘be’, ‘some’, ‘for’, ‘do’, ‘its’, ‘yours’, ‘such’, ‘into’, ‘of’, ‘most’, ‘itself’, ‘other’, ‘off’, ‘is’, ‘s’, ‘am’, ‘or’, ‘who’, ‘as’, ‘from’, ‘him’, ‘each’, ‘the’, ‘themselves’, ‘until’, ‘below’, ‘are’, ‘we’, ‘these’, ‘your’, ‘his’, ‘through’, ‘don’, ‘nor’, ‘me’, ‘were’, ‘her’, ‘more’, ‘himself’, ‘this’, ‘down’, ‘should’, ‘our’, ‘their’, ‘while’, ‘above’, ‘both’, ‘up’, ‘to’, ‘ours’, ‘had’, ‘she’, ‘all’, ‘no’, ‘when’, ‘at’, ‘any’, ‘before’, ‘them’, ‘same’, ‘and’, ‘been’, ‘have’, ‘in’, ‘will’, ‘on’, ‘does’, ‘yourselves’, ‘then’, ‘that’, ‘because’, ‘what’, ‘over’, ‘why’, ‘so’, ‘can’, ‘did’, ‘not’, ‘now’, ‘under’, ‘he’, ‘you’, ‘herself’, ‘has’, ‘just’, ‘where’, ‘too’, ‘only’, ‘myself’, ‘which’, ‘those’, ‘i’, ‘after’, ‘few’, ‘whom’, ‘t’, ‘being’, ‘if’, ‘theirs’, ‘my’, ‘against’, ‘a’, ‘by’, ‘doing’, ‘it’, ‘how’, ‘further’, ‘was’, ‘here’, ‘than’}

        


        




