'''
Created on 2015/12/28

@author: tossy
'''

from WebAPI import Numerous
from Sensors import bme280
from Utility import calculate
import json
import datetime


if __name__ == '__main__':
    nmr = Numerous.Numerous('nmrs_0UNHD4ghOp4s')

    LivingRoomTempID = '3992280136211075389'
    LivingRoomHumidityID = '5954374328040141512'
    LivingRoomPressureID = '8054185316233514131'
    LivingRoomAridityIndexID = '6926013689787547013'
    testMetricID = '9073901838064369747'

    #testValue = '{"value": 777.1}'

    # get current timestamp
    now = datetime.datetime.now()

    # read measurement from BME280 sensor
    currentTemp = bme280.readTemperature()
    currentHumid = bme280.readHumidity()
    currentPres = bme280.readPressure()

    # calculate absolute humidity
    svp = calculate.SaturatedVaporPressure(float(currentTemp))
    vp = calculate.VaporPressure(float(currentHumid), svp)
    ah = calculate.AbsoluteHumidity(float(currentTemp), vp)

    tempValue = {}
    tempValue["value"] = '%.2f' % float(currentTemp)
    tempStrJson = json.dumps(tempValue)

    humidValue = {}
    humidValue["value"] = '%.2f' % float(currentHumid)
    humidStrJson = json.dumps(humidValue)

    presValue = {}
    presValue["value"] = '%.2f' % float(currentPres)
    presStrJson = json.dumps(presValue)

    ahValue = {}
    ahValue["value"] = '%.2f' % ah
    ahStrJson = json.dumps(ahValue)


    # create timestamp string
    strDate = now.strftime('%Y/%m/%d')
    strTime = now.strftime('%H:%M:%S')
    sensorValues = '%.2f\t%.2f\t%.2f\t%.2f' % \
                (float(currentTemp), float(currentHumid), float(currentPres), ah)
    line = strDate + '\t' + strTime + '\t' + sensorValues + '\n'

    # write to log file
    f = open('/home/pi/release/Sensor/sensor.log', 'a')
    f.write(line)
    f.close

    # update each metric value
    nmr.updateMetricValue(LivingRoomAridityIndexID, ahStrJson)
    nmr.updateMetricValue(LivingRoomTempID, tempStrJson)
    nmr.updateMetricValue(LivingRoomHumidityID, humidStrJson)
    nmr.updateMetricValue(LivingRoomPressureID, presStrJson)

    # update photo of Aridity Index depending on its value
    if ah <= 7.0:
        nmr.updateMetricPhoto(LivingRoomAridityIndexID, '/home/pi/release/Sensor/caution.png')
    elif 7.0 < ah <= 11.0:
        nmr.updateMetricPhoto(LivingRoomAridityIndexID, '/home/pi/release/Sensor/warning.png')
    elif ah > 11.0:
        nmr.updateMetricPhoto(LivingRoomAridityIndexID, '/home/pi/release/Sensor/safe.png')
    else:
        pass

