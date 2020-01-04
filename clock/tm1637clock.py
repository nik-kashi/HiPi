#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://raspberrytips.nl/tm1637-4-digit-led-display-raspberry-pi/

import sys
import time
import datetime
import RPi.GPIO as GPIO
import Adafruit_DHT
from lib import tm1637


# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 4


#CLK -> GPIO23 (Pin 16)
#DI0 -> GPIO24 (Pin 18)

Display = tm1637.TM1637(23,24,tm1637.BRIGHT_DARKEST)

Display.Clear()

humidity, temperature = 0 , 0
def render():
    global pin, sensor, humidity, temperature
    seconds=datetime.datetime.now().second
    if seconds%20 == 1 or  seconds%20 == 2:
        showIndoorWeather()
    elif seconds%20 == 8 or seconds%20 == 9:
        showOutdoorWeather()
    elif seconds%20 == 15 or seconds%20 == 16:
        showHumidity()
    else:
        renderClock()
        
    if seconds%20 == 0 :
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def renderClock():
   now = datetime.datetime.now()
   hour = now.hour
   minute = now.minute
   second = now.second
   currenttime = [ int(hour / 10), hour % 10, int(minute / 10), minute % 10 ]

   Display.Show(currenttime)
   Display.ShowDoublepoint(second % 2)

def showIndoorWeather():
    global temperature
    temperature=int(temperature)
    firstNumber= "-" if temperature<0 else int(temperature / 10)
    Display.Show(["i", "n", firstNumber, abs(temperature) % 10 ])
    Display.ShowDoublepoint(True)
    
def showOutdoorWeather():
    temperature=-6
    temperature=int(temperature)
    firstNumber= "-" if temperature<0 else int(temperature / 10)
    Display.Show(["o", "u", firstNumber, abs(temperature) % 10 ])
    Display.ShowDoublepoint(True)
    
def showHumidity():
    global humidity
    humidity=int(humidity)
    firstNumber= "-" if humidity<0 else int(humidity / 10)
    Display.Show(["H", "%", firstNumber, abs(humidity) % 10 ])
    Display.ShowDoublepoint(True)