from cgitb import grey
import tkinter
from tkinter import *
from turtle import bgcolor

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.miliseconds = tkinter.StringVar(value="0")

        self.resizable(False,False)
        self.geometry("443x335")# don t change
        self.frame1 = Frame(self, border=5, bg="green", height=100, width=100)
        self.frame1.pack()



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