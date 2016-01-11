'''
Created on 2015/12/28

@author: tossy
'''

import urllib.request
import base64
import requests
import json

class Numerous:
    '''
    classdocs
    '''


    def __init__(self, key):
        '''
        Constructor
        '''
        self.key = key
        key = key + ":"
        self.authkey = base64.b64encode(key.encode(encoding='utf-8'))
        self.metricURL = "https://api.numerousapp.com/v2/metrics/"
        #self.authheader = "Authorization: Basic " + self.authkey.decode(encoding='UTF-8')
        self.header = {'Content-Type': 'application/json',
                       'Authorization': 'Basic ' + self.authkey.decode(encoding='UTF-8')
                       }

    def updateMetricValue(self, metricID, values):
        '''
        update Metric using metric ID and values (json)
        '''

        url = self.metricURL + metricID + '/events'
        values = values.encode('utf-8')
        req = urllib.request.Request(url, data=values, headers=self.header)
        res = urllib.request.urlopen(req)

    def updateMetricPhoto(self, metricID, filepath):
        '''
        update Metric photo
        '''
        self.header['Content-Type'] = 'multipart/form-data'
        #print(self.header)
        url = self.metricURL + metricID + '/photo'
        #url = 'http://ipv4.fiddler:9080'
        file = {'image': open(filepath, 'rb')}
        #mpart = {'image':('image.img', filepath, "image/jpg")}
        authTuple = (self.key, '')
        res = requests.request('POST', url, auth=authTuple, data=None, files=file, headers=None)
        #return res.status_code

    def fetchMetric(self, metricID):
        '''
        fetch metric data
        '''
        url = self.metricURL + metricID
        req = urllib.request.Request(url, data = None, headers = self.header)

        try:
            res = urllib.request.urlopen(req)
            # need to exclude \n\t from received response data
            data = res.read().decode('utf-8').replace("\n\t","")
            jsonData = json.loads(data)
            #print(jsonData)
            #print(jsonData["photoURL"])
            return jsonData
        except urllib.error.HTTPError as e:
            return 'http status: ' + str(e.code)
