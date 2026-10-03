
# This module is processing the commands sent by the Tkinter GUI
# SirHenricus 9/30/26 - 10/2/26

import os
import sys
import subprocess
from pathlib import Path
import shutil

SCRIPTDIR = Path(__file__).resolve().parent
DFEPATH = "prog/dfe/shock.py"
PJRPATH = "prog/pjr/projectorrays.exe"

TESTFILE1 = "INPUT/DFETEST.app"
TESTFILE2 = "INPUT/PJRTEST.dxr"

DING = "prog/TANG.WAV"

def debugprint(text):
    print("\x1b[35m" + text + "\033[39m")
    sys.stdout.flush()

#-------DIRECTOR EXTRACT

def directorextractrun(file,otherfilemode=False):
    
    #run command
    result = subprocess.run([sys.executable, DFEPATH, file], capture_output=True, text=True)
    subprocess.Popen(["afplay", DING])

    #move folder
    inputfolder = SCRIPTDIR / "INPUT"
    
    if otherfilemode:
     #inputfolder = (SCRIPTDIR / ".." / "INPUT").resolve()
     inputfolder = Path(file).resolve()
     debugprint(f"Global Input mode on!")

    output_dir = SCRIPTDIR / "OUTPUT"
    newfolder = inputfolder / Path(file).stem
    destinationfolder = output_dir /  newfolder.name

    print(f"raw input is {file}")
    print(f"parsed input folder is {inputfolder}")
    print(f"destination folder is {destinationfolder}")
    print(f"newly created folder is {newfolder}")

    # new folder anomaly check
    if newfolder.is_dir():
        if destinationfolder.is_dir():
            debugprint(f"{newfolder} already exists at output!")
            shutil.rmtree(newfolder)
            debugprint(f"Removed {newfolder}")
        else:
            #move new folder to output
            shutil.move(str(newfolder), str(output_dir))

            if destinationfolder.is_dir():
                debugprint(f"{destinationfolder} has been moved to output!")
            else:
                print(f"OOPS! {destinationfolder} could not be moved!")
                shutil.copy(newfolder, destination_dir)
    else:
        print(f"OOPS! New folder was not found at {newfolder}")
        if otherfilemode:
         print("Global file mode enables copy folder movement")
         shutil.copy(inputfolder, destinationfolder)
    
    return result

#-----PROJECTOR RAYS

def projectorraysrun(file,otherfilemode=False):
    #run command
    result = subprocess.run(["/usr/local/bin/wine", PJRPATH, "decompile", file, "-v"], capture_output=True, text=True)
    subprocess.Popen(["afplay", DING])
   
    #move file
    input_folder = inputfolder = SCRIPTDIR / "INPUT"
    if otherfilemode:
     #inputfolder = SCRIPTDIR / ".." / "INPUT"
     inputfolder = SCRIPTDIR / ".."
     debugprint(f"Global Input mode on, folder is {inputfolder}")

    input_folder = input_folder.resolve()
    
    #outputfile = inputfolder / Path(file).stem
    outputfile = Path(file).with_suffix(".dir")
    destination = SCRIPTDIR / "OUTPUT"
    destinationfile = destination / outputfile.name
    #fromdest = inputfolder / outputfile.name 

    # file anomaly check
    if outputfile.is_file():
        if destinationfile.is_file():
            debugprint(f"{destinationfile} already seems to exist")
            outputfile.unlink()
            debugprint("Removed from input!")
        else:
            shutil.move(outputfile, destination)

            if destinationfile.is_file():
                debugprint(f"Moved {destinationfile} to OUTPUT!")
            else:
                print(f"Could not move! {destinationfile} was not found")
    else:
        print(f"Output file was not found at {outputfile}")
        pass

    return result

# this is for when i wanted to test how commands work
def placeholdercmd(file=None):
    subprocess.Popen(["afplay", DING])
    print(f"PLACEHOLDER! {str(file)}")

def winecheck():
    if shutil.which("wine"):
        return True
    else:
        return False

#------TEST MODE

if __name__ == "__main__":
    print("Welcome To Command Testing Mode!")
    
    if (winecheck()):
        print("Wine NOT detected!")
    else:
        print("Wine detected!")
        
    print(" ")

    print(f"SCRIPT DIR is {str(SCRIPTDIR)}")
    print(f"Director files extract path is {DFEPATH}")
    print(f"Projector rays path is {PJRPATH}")
    debugprint("debug prinitng test!")

    print("----------")
    print("1. director files extract")
    print("2. projector rays")
    print("3. ding sound test")

    print("-----------")
    inny = int(input("Type the number of the command to test. Test files will be used"))

    # using match-case wouldn't work
    out = ""
    if inny == 1:
        print("Director Extract Running")
        out = directorextractrun(TESTFILE1)
        print("")
        print("Output: ", out.stdout.strip())
        print("Error: ", out.stderr)
    if inny == 2:
        print("Projector Rays Running")
        print("This may take a little longer")
        out = projectorraysrun(TESTFILE2)
        print("")
        print("Output: ", out.stdout.strip())
        print("Error: ", out.stderr)
    if inny == 3:
        print("ding!")
        placeholdercmd(TESTFILE2)
