import os
import sys

def __main__():
    # handle command line argument if provided.
    if len(sys.argv) > 1:
        HandleChoice(sys.argv[1])
        exit(); 

    #print the build options
    print("build options: ")
    print("[1] Build in debug mode")
    print("[2] Build in release mode")
    print("[3] Abort")

    choice = input("choose a build option: ")
    HandleChoice(choice)
        


def HandleChoice(choice):
    while True:
        try:
            choice = int(choice)
        except ValueError:
            choice = input("must enter a number!! try again.")
            continue
        if choice > 3 or choice < 1:
            choice = input("must choose 1 , 2 or 3. try again")
        else:
            break
    
    

    match choice:
        case 1:
            # Build Debug configuration on Linux using GNU Make
            print("building . . .")
            os.system("premake5 gmake2")
            os.system("make config=debug")
        case 2:
            # Build Release configuration on Linux using GNU Make
            print("building . . .")
            os.system("premake5 gmake2")
            os.system("make config=release")
        case 3:
            print("building process aborted by user.")
            exit(0)


    executablepath = "Debug" if choice == 1 else "Release"
    print("done building.")
    print(f"if no errors accured the executable can be found in the bin/{executablepath}")


    # build executable functions
def build_debug():
    debug_build_btn.config(text='building')
    window.update()
    os.system("premake5 gmake")
    os.system("make config=debug")
    debug_build_btn.config(text="build debug🔨")
    window.update()


def build_release():
    release_build_btn.config(text='building')
    window.update()
    os.system("premake5 gmake")
    os.system("make config=release")
    release_build_btn.config(text="build release📤")
    window.update()


__main__()
