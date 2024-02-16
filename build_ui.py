
import os
import sys
import tkinter as tk
from tkinter import font
import time


def build_debug_linux():
    debug_build_btn.config(text='building')
    window.update()
    os.system("premake5 --os=linux gmake")
    os.system("make config=debug")
    debug_build_btn.config(text="build in debug mode 🔨")
    window.update()


def build_release_linux():
    release_build_btn.config(text='building')
    window.update()
    os.system("premake5 --os=linux gmake")
    os.system("make config=release")
    release_build_btn.config(text="build in release mode 📤")
    window.update()

window = tk.Tk()
greeting = tk.Label(window, text="c++ project builder")
debug_build_btn = tk.Button(window, text="build in debug mode 🔨", command=build_debug_linux)
release_build_btn = tk.Button(window, text="build in release mode 📤", command=build_release_linux)


def __main__():
    print(font.families())
    windowbg = "#444444"  # dark grey
    buttonbg = "#bbbbbb"
    # modify main window
    window.geometry("1240x720")
    window.config(bg=windowbg)
    window.title('c++ project builder')
    window.resizable(False, False)
    # modify title label
    greeting.config(font=('David', 35, 'bold'), bg=windowbg, fg='red')
    greeting.place(x=300, y=20)
    debug_build_btn.place(x=200, y=350)
    debug_build_btn.config(bg=buttonbg, font=('David', 20), width=20, height=1)
    release_build_btn.place(x=600, y=350)
    release_build_btn.config(bg=buttonbg, font=('David', 20), width=20, height=1)
    window.mainloop()


__main__()
