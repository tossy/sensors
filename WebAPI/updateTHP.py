#!/usr/bin/python
'''
update temperature, humidity, pressure from IFTTT service
'''
from Sensors import bme280
import urllib

temp =  bme280.readTemperature() 
hum  =  bme280.readHumidity()
pres =  bme280.readPressure()

key = "dspYFqHroQX45y-4WwoIfS"
event1 = "LivingRoomTemp"
event2 = "LivingRoomHumidity"
event3 = "LivingRoomPressure"
reqURL1 = "https://maker.ifttt.com/trigger/" + event1 + "/with/key/" + key
reqURL2 = "https://maker.ifttt.com/trigger/" + event2 + "/with/key/" + key
reqURL3 = "https://maker.ifttt.com/trigger/" + event3 + "/with/key/" + key
header = {"Content-Type": "application/json"}

temp_values = {'value1':temp}
hum_values =  {'value1':hum}
pres_values = {'value1':pres}

temp_data = urllib.parse.urlencode(temp_values)
hum_data  = urllib.parse.urlencode(hum_values)
pres_data = urllib.parse.urlencode(pres_values)

req1 = urllib.request.Request(reqURL1, temp_data)
res1 = urllib.request.urlopen(req1)

req2 = urllib.request.Request(reqURL2, hum_data)
res2 = urllib.request.urlopen(req2)

req3 = urllib.request.Request(reqURL3, pres_data)
res3 = urllib.request.urlopen(req3)


