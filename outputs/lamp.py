import os

os.system("gpio export 26 out")


def turn_on(fade_in_duration=0):
    os.system("gpio -g write 26 1")


def turn_off(fade_out_duration=0):
    os.system("gpio -g write 26 0")
