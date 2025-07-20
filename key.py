from pynput import keyboard
from collections import defaultdict
import pickle
import os



keycount = defaultdict(int)
if os.path.exists("keydata.pkl"):
    with open("keydata.pkl","rb") as f:
        keycount.update(pickle.load(f))


def on_press(key,injected):
    try:
        keycount[key.char.lower()]+=1
    except AttributeError:
        keycount[str(key)]+=1 

    with open("keydata.pkl" ,"wb") as f:
        pickle.dump(dict(keycount),f)


listerner = keyboard.Listener(on_press=on_press)

listerner.start()

print("starting to count ur key press")
listerner.join()