
from pynput.keyboard import Listener, Key,Controller
import time

def anonymous(key):
    key = str(key)
    if key =="Key.esc":
        return False
    
with Listener(on_press=anonymous) as Listener:
    Listener.join()


