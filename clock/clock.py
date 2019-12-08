# Pedro Rodrigues

import time
import os
import datetime
import ctypes
import platform
import textwrap

opsys = platform.platform()
if opsys == 'Windows':
    ctypes.windll.kernel32.SetConsoleTitleA("Python Clock")
    # Changes terminal size
    os.system("mode con: cols=90 lines=11")

list = [
    textwrap.dedent('''
 $$$$$$\\
$$$ __$$\\
$$$$\ $$ |
$$\$$\$$ |
$$ \$$$$ |
$$ |\$$$ |
\$$$$$$  /
 \______/'''),
    textwrap.dedent('''
  $$\\
$$$$ |
\_$$ |
  $$ |
  $$ |
  $$ |
$$$$$$\\
\______|'''),

    textwrap.dedent('''
  $$$$$$\\
$$  __$$\\
\__/  $$ |
 $$$$$$  |
$$  ____/
$$ |
$$$$$$$$\\
\________|'''),
    textwrap.dedent('''
 $$$$$$\\
$$ ___$$\\
\_/   $$ |
  $$$$$ /
  \___$$\\
$$\   $$ |
\$$$$$$  |
 \______/'''),
    textwrap.dedent('''
$$\   $$\\
$$ |  $$ |
$$ |  $$ |
$$$$$$$$ |
\_____$$ |
      $$ |
      $$ |
      \__|'''),
    textwrap.dedent('''
$$$$$$$\\
$$  ____|
$$ |
$$$$$$$\\
\_____$$\\
$$\   $$ |
\$$$$$$  |
 \______/ '''),
    textwrap.dedent('''
 $$$$$$\\
$$  __$$\\
$$ /  \__|
$$$$$$$\\
$$  __$$\\
$$ /  $$ |
 $$$$$$  |
 \______/ '''),
    textwrap.dedent('''
$$$$$$$$\\
\____$$  |
    $$  /
   $$  /
  $$  /
 $$  /
$$  /
\__/'''),
    textwrap.dedent('''
 $$$$$$\\
$$  __$$\\
$$ /  $$ |
 $$$$$$  |
$$  __$$<
$$ /  $$ |
\$$$$$$  |
 \______/ '''),
    textwrap.dedent('''
 $$$$$$\\
$$  __$$\\
$$ /  $$ |
\$$$$$$$ |
 \____$$ |
$$\   $$ |
\$$$$$$  |
 \______/ ''')
]

colon = '''

  
   $$\\
   \__|
   
   $$\\
   \__|'''
messages = {}
loopI = 0

def setMsg(key, value):
    global messages
    messages[key] = value


def removeMsg(key):
    global messages
    messages.pop(key)


def renderClock():
    global opsys
    global list
    global colon
    global loopI

    loopI += 1
    if opsys == 'Windows':
        os.system('cls')
    else:
        print("\n" * 15)

    ti = str(datetime.datetime.now())
    ti = ti[11:16]

    lines = ["", "", "", "", "", "", "", "", ""]
    line = 0

    numbers = [[], [], [], [], [], [], [], []]
    for x in range(5):
        if ti[x].isdigit():
            # print list[x]
            numbers[x] = list[int(ti[x])].splitlines()
        elif ti[x] == ":":
            numbers[x] = colon.splitlines()

    for x in range(9):
        temp = ""
        for i in range(9):
            # print x,i
            try:
                if i == 8:
                    temp += str(numbers[i][line])
                else:
                    temp += str(numbers[i][line]).ljust(10)
            except:
                temp += "          "
        lines[x] += temp
        line += 1

    # print lines

    for x in range(9):
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
