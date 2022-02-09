from cgitb import grey
import tkinter
from tkinter import *
from turtle import bgcolor

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.miliseconds = tkinter.StringVar(value="0")

        self.overrideredirect(True)
        self.attributes('-topmost', 1)
        self.iconbitmap('./assets/click_icon.ico')
        self.title("Auto Clicker 1.0")

        self.resizable(False,False)
        self.geometry('443x335')# don t change +0+0

        self.title_bar = Frame(self, bg='white', bd=1)
        close_button = Button(self.title_bar, text='X', command=self.destroy)
        window = Canvas(self, bg='#f0f0f0')

        # pack the widgets
        self.title_bar.pack(side=TOP, fill=X)
        close_button.pack(side=RIGHT)
        window.pack(expand=1, fill=BOTH)

        # moving the window
        self.title_bar.bind('<Button-1>', self.get_pos)
        
        self.frame1 = LabelFrame(window, height=44, text="Click interval")
        self.frame1.pack(fill=X, padx=2, pady=2)

        #LabelFrame(self, text="This is a LabelFrame").pack(fill=X)
        #labelframe.pack(fill="both", expand="yes")

    def get_pos(self, event):
        xwin = self.winfo_x()
        ywin = self.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx


        def move_window(event1):
            self.geometry("443x335" + '+{0}+{1}'.format(event1.x_root + xwin, event1.y_root + ywin))

        self.title_bar.bind('<B1-Motion>', move_window)


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