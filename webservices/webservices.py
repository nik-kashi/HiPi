from subprocess import check_output
import json


def getOutdoorTemprature():
    try:
        weatherObject = check_output(
            ['curl',
             'api.openweathermap.org/data/2.5/weather?id=2753355&appid=2c7874d24ca6af575f6eae4a897583ff&units=metric'])
        return int(json.loads(weatherObject)['main']['temp'])
    except:
        return 99


def farenheitToCelsius(f):
    return (f - 32) * 5 / 9
