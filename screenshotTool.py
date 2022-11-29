import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name = 'C:/DYPSOE/TY/1Pythonprojects/screenshots/{}.png'.format(name)
    #time.sleep(3) - to create delay after clicking button to take ss
    img = pyautogui.screenshot(name)
    img.show

screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text = 'Screenshot',command=screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(frame, text = 'Exit', command = quit)

close.pack(side=tk.LEFT)

root.mainloop()


