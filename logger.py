from pynput.keyboard import Key, Listener # pip install pynput

keys = []

def on_press(e):
    global keys # accessing the global keys array
    keys.append(e) # add the pressed key to the array

with Listener(on_press = on_press) as listener:
    listener.join()

    