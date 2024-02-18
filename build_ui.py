import os
import sys
import tkinter as tk
import time


def __main__():
    # declare window and widgets and colors
    global window
    global title
    global debug_build_btn
    global release_build_btn
    global current_os
    global os_dropdown
    windowbg = "#444444"  # dark grey
    buttonbg = "#bbbbbb"  # light grey
    # define window and widgets
    window = tk.Tk()
    title = tk.Label(window, text="C++ project builder")
    debug_build_btn = tk.Button(window, text="build in debug mode 🔨", command=build_debug)
    release_build_btn = tk.Button(window, text="build in release mode 📤", command=build_release)
    current_os = tk.StringVar(window)
    os_dropdown = tk.OptionMenu(window, current_os, 'linux', 'windows')
    os_menu = window.nametowidget(os_dropdown.menuname)
    # modify main window
    window.geometry("1240x720")
    window.config(bg=windowbg)
    window.title('C++ project builder')
    window.resizable(False, False)
    # modify title label
    title.config(font=('David', 35, 'bold'), bg=windowbg, fg='red')
    title.place(x=300, y=20)
    debug_build_btn.place(x=200, y=350)
    debug_build_btn.config(bg=buttonbg, font=('David', 20), width=20, height=1)
    release_build_btn.place(x=600, y=350)
    release_build_btn.config(bg=buttonbg, font=('David', 20), width=20, height=1)
    # modify os_dropdown menu
    current_os.set(sys.platform)
    os_dropdown.config(font=('David', 20), bg='black', fg='white')
    os_menu.config(font=('David', 20), bg='black', fg='white')
    os_dropdown.place(x=950, y=0)
    window.mainloop()


def build_debug():
    debug_build_btn.config(text='building')
    window.update()
    os.system("premake5 --os=" + current_os.get() + " gmake")
    os.system("make config=debug")
    debug_build_btn.config(text="build in debug mode 🔨")
    window.update()


def build_release():
    release_build_btn.config(text='building')
    window.update()
    os.system("premake5 --os=" + current_os.get() + "  gmake")
    os.system("make config=release")
    release_build_btn.config(text="build in release mode 📤")
    window.update()


__main__()
