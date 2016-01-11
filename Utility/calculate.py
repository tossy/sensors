# conding:utf-8
'''
Created on 2015/12/28

@author: tossy
@note: equations are based on the web page http://www.daiichi-kagaku.co.jp/situdo/notes/note108.html
'''

import math

def SaturatedVaporPressure(temp):
    '''
    @param temp: temperature in Celcius
	@return: saturated vapor pressure in hPa
    '''
    T = temp + 273.15
    
    return math.exp(-6096.9385 * T ** -1 + 21.2409642 - 
                    2.711193 * 10 ** -2 * T + 
                    1.673952 * 10 ** -5 * T ** 2 +
                    2.433502 * math.log(T))
    
    #return 6.11 * 10 ** (7.5 * temp / (237.3 + temp)) 

def VaporPressure(rh, svp):
    '''
    @param rh: relative humidity in %
    @param svp: saturated vapor pressure in hPa
	@return: vapor pressure in hPa
    '''
    return svp * rh / 100
    

def AbsoluteHumidity(temp, vp):
    '''
    @param temp: temperature in Celcius
    @param vp: vapor pressure in hPa
    @return: absolute humidity in g/m^3
    '''
    #return vp * 100 / (8.31447 * (273.15 + temp) * 18)
    return 0.794 * 10 ** -2 * vp / (1 + 0.00366 * temp)
