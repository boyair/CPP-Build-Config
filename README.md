# CPP-Build-Config
A base for building c++ applications for linux in a simple project build.
This project exists as an easy way to start making C++ project without using
an IDE and without having to learn cmake or premake from the get go.

## system requirements
to make building possible you must have the following packages on your linux system:
python with ktinker library (for GUI)
premake5
gcc compiler


## How to use
1. Clone this repo where you want to start your project.
2. for linking external libraries edit the "links{}" sections inside the premake5.lua file.
3. if you want to add more .cpp or .h files add them inside the src folder.
4. run the build.py script by typing the command "python build_headless.py" or "python build_ui.py".
5. choose your build option in the menu and press ENTER.
6. find your executable inside bin/Debug or bin/Release (according to your build choice).

by default any libraries placed in dependencies/linux/lib 
and any include files located in dependencies/linux/include
will be automatically added to your project.
