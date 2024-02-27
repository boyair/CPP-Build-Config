import os
import sys
import tkinter as tk
import subprocess


def __main__():
    # declare window, widgets and colors (necessary to make them global)
    global window
    global title
    global debug_build_btn
    global release_build_btn
    global debug_run_btn
    global release_run_btn
    global cl_args_label
    global cl_args_input
    windowbg = "#444444"  # dark grey
    buttonbg = "#bbbbbb"  # light grey
    # define window and widgets
    window = tk.Tk()
    title = tk.Label(window, text="C++ project\n builder",
                     font=('David', 35, 'bold'), bg=windowbg, fg='red')
    debug_build_btn = tk.Button(window, text="build debug🔨", command=build_debug,
                                bg=buttonbg, font=('David', 20), width=14, height=1)
    release_build_btn = tk.Button(window, text="build release📤", command=build_release,
                                  bg=buttonbg, font=('David', 20), width=14, height=1)
    debug_run_btn = tk.Button(window, text="RUN", command=run_debug,
                              bg=buttonbg, font=('David', 20), width=4, height=1)
    release_run_btn = tk.Button(window, text="RUN", command=run_release,
                                bg=buttonbg, font=('David', 20), width=4, height=1)
    cl_args_label = tk.Label(window, text="command line args:",
                             font=('David', 20, 'bold'), bg=windowbg, fg='black')
    cl_args_input = tk.Text(window, height=2, width=20,
                            bg='black', fg='white', font=('David', 20))
    # modify main window
    window.config(bg=windowbg, width=8, height=3)
    window.geometry("350x520")
    window.title('C++ project builder')
    window.resizable(False, False)
    # place labels
    title.place(x=30, y=10)
    cl_args_label.place(x=0, y=350)
    # place buttons
    debug_build_btn.place(x=10, y=200)
    release_build_btn.place(x=10, y=300)
    debug_run_btn.place(x=255, y=200)
    release_run_btn.place(x=255, y=300)
    # place cl_args_input
    cl_args_input.place(x=10, y=400)
    window.mainloop()


    # build executable functions
def build_debug():
    debug_build_btn.config(text='building')
    window.update()
    os.system("premake5 gmake2")
    os.system("make config=debug")
    debug_build_btn.config(text="build debug🔨")
    window.update()


def build_release():
    release_build_btn.config(text='building')
    window.update()
    os.system("premake5 gmake2")
    os.system("make config=release")
    release_build_btn.config(text="build release📤")
    window.update()


    # run executable functions
def run_debug():
    release_run_btn.config(text='...')
    window.update()
    exec_file = "Application" if sys.platform == "linux" else "Application.exe"
    os.system("bin/Debug/" + exec_file + " " + cl_args_input.get("1.0","end-1c"))
    release_run_btn.config(text='RUN')
    window.update()


def run_release():
    release_run_btn.config(text='...')
    window.update()
    exec_file = "Application" if sys.platform == "linux" else "Application.exe"
    os.system("bin/Release/" + exec_file + " " + cl_args_input.get("1.0","end-1c"))
    release_run_btn.config(text='RUN')
    window.update()


__main__()
