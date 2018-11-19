import psycopg2
import psycopg2.extensions


conn = psycopg2.connect("dbname=TravelBot user=postgres password=Database!12")
cur = conn.cursor()
#insert_query = "INSERT INTO messages(id,createdate,source,destination,travel_date,passenger_ct,pref_airlines)VALUES(random(),current_date,'SFO','ATL','2018-08-21',1,'UA')"
#insert_query="INSERT INTO flight_details (flights_id,flights_res,msg_id)VALUES(random(),'25',1)"

#insert_query= "UPDATE hotel_details SET hotel_id = '1' WHERE msg_id = '1'";
insert_query="select * from messages"
cur.execute(insert_query)
result = cur.fetchall()
print (result)
conn.commit()