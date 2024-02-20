import os
import sys
import tkinter as tk
import subprocess


def __main__():
    # declare window, widgets and colors
    global window
    global title
    global debug_build_btn
    global release_build_btn
    global debug_run_btn
    global release_run_btn
    global current_os
    global os_dropdown
    global os_text
    windowbg = "#444444"  # dark grey
    buttonbg = "#bbbbbb"  # light grey
    # define window and widgets
    window = tk.Tk()
    title = tk.Label(window, text="C++ project\n builder")
    debug_build_btn = tk.Button(window, text="build debug🔨", command=build_debug)
    release_build_btn = tk.Button(window, text="build release📤", command=build_release)
    debug_run_btn = tk.Button(window, text="RUN", command=run_debug)
    release_run_btn = tk.Button(window, text="RUN", command=run_release)
    current_os = tk.StringVar(window)
    os_dropdown = tk.OptionMenu(window, current_os, 'linux', 'windows')
    os_menu = window.nametowidget(os_dropdown.menuname)
    os_text = tk.Label(window, text="OS:")
    current_os.set(sys.platform)
    # modify main window
    window.geometry("350x520")
    window.config(bg=windowbg, width=8, height=3)
    window.title('C++ project builder')
    window.resizable(False, False)
    # modify title label
    title.config(font=('David', 35, 'bold'), bg=windowbg, fg='red')
    title.place(x=30, y=10)
    debug_build_btn.config(bg=buttonbg, font=('David', 20), width=14, height=1)
    debug_build_btn.place(x=10, y=200)
    release_build_btn.config(bg=buttonbg, font=('David', 20), width=14, height=1)
    release_build_btn.place(x=10, y=300)
    debug_run_btn.config(bg=buttonbg, font=('David', 20), width=4, height=1)
    debug_run_btn.place(x=255, y=200)
    release_run_btn.config(bg=buttonbg, font=('David', 20), width=4, height=1)
    release_run_btn.place(x=255, y=300)
    # modify os_dropdown menu
    os_text.config(font=('David', 30, 'bold'), bg=windowbg, fg='black')
    os_menu.config(font=('David', 20), bg='black', fg='white')
    os_dropdown.config(font=('David', 20), bg='black', fg='white')
    os_dropdown.place(x=70, y=405)
    os_text.place(x=0, y=400)
    window.mainloop()


def build_debug():
    debug_build_btn.config(text='building')
    window.update()
    print(current_os.get())
    os.system("rm -rf obj/Debug")
    os.system("premake5 --os=" + current_os.get() + " gmake")
    os.system("make config=debug")
    debug_build_btn.config(text="build debug🔨")
    window.update()


def build_release():
    release_build_btn.config(text='building')
    window.update()
    print(current_os.get())
    os.system("rm -rf obj/Release")
    os.system("rm Makefile")
    os.system("premake5 --os=" + current_os.get() + "  gmake")
    os.system("make config=release")
    release_build_btn.config(text="build release📤")
    window.update()


def run_debug():
    release_run_btn.config(text='...')
    window.update()
    command = "bin/Debug/Application" if current_os.get() == "linux" else "bin/Debug/Application.exe"
    print(command)
    os.system(command)
    release_run_btn.config(text='RUN')
    window.update()


def run_release():
    release_run_btn.config(text='...')
    window.update()
    command = "bin/Release/Application" if current_os.get() == "linux" else "bin/Release/Application.exe"
    os.system(command)
    release_run_btn.config(text='RUN')
    window.update()


__main__()
