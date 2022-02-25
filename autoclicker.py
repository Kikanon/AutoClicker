from cgitb import grey
import tkinter
from tkinter import *
import tkinter.font
from turtle import back, bgcolor

from matplotlib.pyplot import fill

class App(tkinter.Tk):
    window_size = '442x365'

    def __init__(self):
        super().__init__()
        self.miliseconds = tkinter.StringVar(value="0")

        self.attributes('-topmost', 1)
        self.title("Auto Clicker 1.0")

        self.resizable(False,False)
        self.geometry(self.window_size)# don t change +0+0

        # todo: https://stackoverflow.com/questions/4066027/making-tkinter-windows-show-up-in-the-taskbar

        gray_area = Canvas(self, bg='#f0f0f0')

        # pack the widgets
        gray_area.pack(expand=1, fill=BOTH)
            
        
        self.frame1 = LabelFrame(gray_area, height=44, text="Click interval")
        self.frame1.pack(fill=X, padx=2, pady=2)

        Entry(self.frame1, width=7).pack(side=LEFT)
        Label(self.frame1, text="hours").pack(side=LEFT)
        Entry(self.frame1, width=7).pack(side=LEFT)
        Label(self.frame1, text="mins").pack(side=LEFT)
        Entry(self.frame1, width=7).pack(side=LEFT)
        Label(self.frame1, text="secs").pack(side=LEFT)
        Entry(self.frame1, width=7).pack(side=LEFT)
        Label(self.frame1, text="miliseconds").pack(side=LEFT)

        self.frame2 = LabelFrame(gray_area, height=44, text="Click options")

        self.frame3 = LabelFrame(gray_area, height=44, text="Click repeat")

        self.frame2.pack(side=LEFT, padx=2, pady=2, fill=X)
        self.frame3.pack(side=LEFT, padx=2, pady=2, fill=X)

        Entry(self.frame2, width=7).pack(side=LEFT)
        Label(self.frame2, text="hours").pack(side=LEFT)

        #LabelFrame(self, text="This is a LabelFrame").pack(fill=X)
        #labelframe.pack(fill="both", expand="yes")

if __name__ == '__main__':
    myApp = App()
    myApp.mainloop()

"""
from pynput import keyboard, mouse
import time
import threading

stop = True
started = True

def jitter():
    mouse1 = mouse.Controller()
    keyb = keyboard.Controller()
    while stop:
        print('loop')
        time.sleep(0.5)
        mouse1.press(mouse.Button.right)
        time.sleep(0.1)
        keyb.press('e')
        time.sleep(0.1)
        


b = threading.Thread(name='background', target=jitter)


def loop():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def on_press(key):
    global started
    print("something happened")
    if key == keyboard.Key.left:
        stop=False

    if (key == keyboard.Key.right) & started:
        b.start()
        started = False
        print("start jitter")


f = threading.Thread(name='foreground', target=loop)

f.start()

print('app started')


"""