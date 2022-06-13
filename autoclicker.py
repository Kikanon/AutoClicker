from cgitb import grey
from msilib.schema import RadioButton
import tkinter
from tkinter import *
import tkinter.font
from turtle import back, bgcolor, width
import os

from matplotlib.pyplot import fill

class TaskBar(Tk):    
    def __init__(self):
        Tk.__init__(self)
        self.attributes('-alpha', 0.0)

class App(tkinter.Tk):
    window_size = '442x365'

    def __init__(self):
        super().__init__()
        self.miliseconds = tkinter.StringVar(value="0")

        self.iconbitmap(default=os.path.abspath("./assets/click_icon.ico"))

        self.attributes('-topmost', 1)
        self.title("Auto Clicker 1.0")

        self.resizable(False,False)
        self.geometry(self.window_size)# don t change +0+0

        self.repeatSelection=IntVar()
        self.mouseButtonSelection=StringVar()
        self.mouseButtonSelection.set("Left")
        self.mouseClickSelection=StringVar()
        self.mouseClickSelection.set("Single")
        gray_area = Canvas(self, bg='#f0f0f0')

        # pack the widgets
        gray_area.pack(expand=1, fill=BOTH)
            
        frame1 = LabelFrame(gray_area, height=44, text="Click interval")
        frame1.pack(fill=X, padx=2, pady=2)

        Entry(frame1, width=7).pack(side=LEFT)
        Label(frame1, text="hours").pack(side=LEFT)
        Entry(frame1, width=7).pack(side=LEFT)
        Label(frame1, text="mins").pack(side=LEFT)
        Entry(frame1, width=7).pack(side=LEFT)
        Label(frame1, text="secs").pack(side=LEFT)
        Entry(frame1, width=7).pack(side=LEFT)
        Label(frame1, text="miliseconds").pack(side=LEFT)

        optionsFrame = Frame(gray_area, height=45)
        frame2 = LabelFrame(optionsFrame, text="Click options")
        frame3 = LabelFrame(optionsFrame, text="Click repeat")
        positionFrame = LabelFrame(gray_area, height=50, text="Cursor position", borderwidth=2, relief="groove")
        buttonsFrame = Frame(gray_area,height=50, borderwidth=2, relief="groove")

        optionsFrame.pack(fill=X)
        positionFrame.pack(fill=X)
        buttonsFrame.pack(fill=X)
        frame2.pack(padx=2, pady=2, expand=True, fill=BOTH, side=LEFT)
        frame3.pack(padx=2, pady=2, expand=True, fill=BOTH, side=LEFT)

        options1 = Frame(frame2)
        options2 = Frame(frame2)
        options1.pack(side=TOP)
        options2.pack(side=TOP)

        Label(options1, text="Mouse button: ").pack(side=LEFT)
        OptionMenu(options1, self.mouseButtonSelection, "Left", "Right", "Middle").pack(side=LEFT)

        Label(options2, text="Click type: ").pack(side=LEFT)
        OptionMenu(options2, self.mouseClickSelection, "Single", "Double").pack(side=LEFT)

        repeatOptions1 = Frame(frame3)
        repeatOptions2 = Frame(frame3)
        repeatOptions1.pack(side=TOP)
        repeatOptions2.pack(side=TOP)

        Radiobutton(repeatOptions1, text="Repeat", variable=self.repeatSelection, value=1).pack(side=LEFT)
        Radiobutton(repeatOptions2, text="Repeat until stopped", variable=self.repeatSelection, value=2).pack()

        Entry(repeatOptions1, width=7).pack(side=LEFT)
        Label(repeatOptions1, text="times").pack(side=LEFT)

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