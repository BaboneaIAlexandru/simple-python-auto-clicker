from time import sleep
from threading import Thread,Event
from pynput.keyboard import Listener,Key
from pynput.mouse import Controller,Button

mouse=Controller()
mouseButton=Button.left

delay=5
clickerActive=False
start_stop_key=Key.f4
exit_key=Key.esc

stop_event=Event()

def checkPressedKey(pressedKey):
    global clickerActive
    if pressedKey==start_stop_key:
        clickerActive=not clickerActive
        if not clickerActive:
            stop_event.set()
    elif pressedKey==exit_key:
        clickerActive=False
        stop_event.set()
        return False
    
def autoClicker():
    while True:
        if clickerActive:
            mouse.click(mouseButton)
            stop_event.clear()
            stop_event.wait(delay)
        else:
            sleep(0.1)

Thread(target=autoClicker,daemon=True).start()

with Listener(on_press=checkPressedKey) as listener:
    listener.join()




