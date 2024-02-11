# CPP-Build-Config
A base for building c++ applications for windows and linux in a simple project build.
Using premake5 for creating Makefile and using a python script for simple CLI.


## How to use
1. Clone this repo where you want to start your project.
2. for linking external libraries edit the "links{}" sections.
3. any code files you wish to add you place in the given src folder.
4. run the build.py script by typing the command "python build.py" (on windows you can simply double click it if you have python installed).
5. choose your build option in the menu and press ENTER.
6. find your executable inside bin/Debug or bin/Release (according to your build choice).

** windows dependencies can be placed in a folder called WinDependencies and will be linked by default.
