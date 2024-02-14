import os
import sys

def __main__():
    if sys.platform == "linux":
        # handle command line argument if provided.
        if len(sys.argv) > 1:
            HandleChoiceLinux(sys.argv[1])
            exit(); 

        #print the build options
        print("build options: ")
        print("1: Developer (build in debug mode)")
        print("2: User (build in release mode)")
        print("3: Abort")

        choice = input("choose a build option: ")
        HandleChoiceLinux(choice)
        
    elif sys.platform == "win32":
        os.system("premake5-windows.exe --os=windows vs2022")

        print("done creating solution")
        print("if no errors accured you can open game.sln file with visual studio 2022 or later and build the project from there.")

    else:
        print("Operating system not supported...\n the build system only support windows and linux.")



def HandleChoiceLinux(choice):
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
            os.system("premake5 --os=linux gmake")
            os.system("make config=debug")
        case 2:
            # Build Release configuration on Linux using GNU Make
            print("building . . .")
            os.system("premake5 --os=linux gmake")
            os.system("make config=release")
        case 3:
            print("building process aborted by user.")
            exit(0)


    executablepath = "Debug" if choice == 1 else "Release"
    print("done building.")
    print(f"if no errors accured the executable can be found in the bin/{executablepath}")


__main__()
