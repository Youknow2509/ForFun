from pynput.keyboard import Key, Controller, Listener
import time


keyboard = Controller()


while True:
    keyboard.type('%fish')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2.8)
    # if on_press =="Key.esc":
    #     break



