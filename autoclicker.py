from time import sleep
from threading import Thread
from pynput.keyboard import Listener,Key
from pynput.mouse import Controller,Button

mouse=Controller()
mouseButton=Button.left

delay=1
clickerActive=False
start_stop_key=Key.f4
exit_key=Key.esc

def checkPressedKey(pressedKey):
    global clickerActive
    if pressedKey==start_stop_key:
        clickerActive=not clickerActive
    elif pressedKey==exit_key:
        return False
    
def autoClicker():
    while True:
        if clickerActive:
            mouse.click(mouseButton)
            sleep(delay)
        else:
            sleep(0.1)

Thread(target=autoClicker,daemon=True).start()

with Listener(on_press=checkPressedKey) as listener:
    listener.join()
