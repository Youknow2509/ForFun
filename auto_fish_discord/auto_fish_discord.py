from pynput.keyboard import Key, Controller, Listener
import time


keyboard = Controller()
print("Lệnh spam câu cá %fish, lặp 2.8 s")
while True:
    keyboard.type('%fish')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2.8)
    # if on_press =="Key.esc":
    #     break



