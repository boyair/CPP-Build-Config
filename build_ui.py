
import os
import sys
import tkinter as tk
import time

def __main__():
    window = tk.Tk()
    window.geometry("1240x720")
    window.config(bg='green')
    greeting = tk.Label(window, text="CPP project builder")
    greeting.config(font=('David', 20))
    greeting.config(bg='green', fg='red')
    greeting.place(x=400, y=20)
    debug_build = tk.Button(window, text="build in debug mode.")
    debug_build.place(x=200, y=350)

    window.mainloop()

__main__()
