from time import sleep
from outputs import radio, lamp
from clock import clock,tm1637clock
import json
import schedule


def checkForEvents():
    pass


def play_radio():
    radio.play()
    lamp.turn_on()
    clock.setMsg("Radio", "Sky Radio NL.")


with open('/home/pi/HiPi/config.json') as json_file:
    conf = json.load(json_file)
alarms = conf["alarms"]
print(len(alarms), "alarms loaded")
for alarm in alarms:
    clock.setMsg(alarm["title"], "will be run at " + alarm["time"] + " of " + ','.join(alarm["repeat"]))
    schedule.every().day.at(alarm["time"]).do(job_func=play_radio)

while True:
    checkForEvents()
    # clock.renderClock()
    tm1637clock.render()
    sleep(1)
    schedule.run_pending()
