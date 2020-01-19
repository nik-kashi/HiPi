# Pedro Rodrigues

import time
import os
import datetime
import ctypes
import platform

from clock.clock_font import normal_font, outline_font, superbig_font

opsys = platform.platform()
if opsys == 'Windows':
    ctypes.windll.kernel32.SetConsoleTitleA("Python Clock")
    # Changes terminal size
    os.system("mode con: cols=90 lines=11")

messages = {}
loopI = 0


def setMsg(key, value):
    global messages
    messages[key] = value


def removeMsg(key):
    global messages
    messages.pop(key)


font = outline_font


def renderClock():
    global opsys
    global font
    global colon
    global loopI

    loopI += 1
    if opsys == 'Windows':
        os.system('cls')
    else:
        print("\n" * 15)

    ti = str(datetime.datetime.now())
    ti = ti[11:16]
    font_height = font.height_in_lines
    lines = [""] * (font_height + 1)
    line = 0

    numbers = [[], [], [], [], [], [], [], []]
    for x in range(5):
        if ti[x].isdigit():
            # print list[x]
            numbers[x] = font.numbers[int(ti[x])].splitlines()
        elif ti[x] == ":":
            numbers[x] = font.colon.splitlines()

    for x in range(font_height + 1):
        temp = ""
        for i in range(font_height + 1):
            # print x,i
            try:
                if i == font_height:
                    temp += str(numbers[i][line])
                else:
                    temp += str(numbers[i][line]).ljust(10)
            except:
                temp += "          "
        lines[x] += temp
        line += 1

    # print lines

    for x in range(font_height + 1):
        print(lines[x])

    print(getProperMsg(loopI))


def getProperMsg(i):
    global messages
    messages_len = len(messages)
    if messages_len == 0:
        return ""
    msgasList = []
    for msgItem in messages.items():
        msgasList.append(msgItem)
    # dirty hack because  List(messages.items()) does not works!

    msg = msgasList[i % messages_len]
    return str(msg[0] + " : " + msg[1])
