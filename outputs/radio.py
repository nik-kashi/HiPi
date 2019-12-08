from subprocess import Popen

running_process_on_os = None
running = False


def play():
    global running
    global running_process_on_os
    if not running:
        running_process_on_os = Popen(['mpg123', 'http://20073.live.streamtheworld.com/SKYRADIO.mp3'])
        running = True
    else:
        print("radio already ran")


def stop():
    global running
    global running_process_on_os
    if running:
        running_process_on_os.terminate()
        running = False
