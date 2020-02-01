""" This is the worker program which does everything """
import requests
import tverketheader
import tverketresponse
import dbhelper
import time
import mysql
import time

# Why ?. because in docker mysql service will take some time to init.
time.sleep(10)

# Create DB
cnx = mysql.connector.connect(host="db", user='user', password="test")
mycursor = cnx.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS trafikverket")
cnx.commit()
cnx.close()

# Create table
cnx = mysql.connector.connect(host="db", user='user', password="test", database='trafikverket')
mycursor = cnx.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS trafficflow (id INT AUTO_INCREMENT PRIMARY KEY, flow INT(6), speed INT(6), time VARCHAR(30))")
cnx.commit()
cnx.close()

# The trafikverkt api 
url = "https://api.trafikinfo.trafikverket.se/v1/data.json"

# @ToDo i am looking for specific site. Hard code it now. Move it as program arg later. Compose header and body

flow = tverketheader.TrafficFlowCompose(regionid=4, county=1, site=914)
data_to_send = flow.compose_body()
headers = flow.compose_header()

# Run this in an infinite loop and poll every hour
while True:

	# Send HTTP POST request and get response
	response = requests.post(url, data=data_to_send, headers=headers)
	json_response = response.json()
	print(json_response)
	# Frame response object
	response = tverketresponse.TrafficFlowResponse(json_response)

	# push to db
	dbobj = dbhelper.DbHelper(response)
	dbobj.push_data()
	# Sometimes data may not be updated for long time which will cause redundant entries.
	dbobj.remove_duplicates()
	# sleep
	time.sleep(60)
