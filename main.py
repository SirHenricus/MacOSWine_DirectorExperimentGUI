
# SirHenricus On GitHub 9/30/26, 10/1, 10/2
# Meant for 3.14.3, Optimized for MacOS Users
# YOU WILL NOT BE ABLE TO USE THIS IF YOU DON'T HAVE WINE
# No AI was used to make any of this

import tkinter as tk
from tkinter import ttk
from ToggledFrame import *

import commandrun as cmd
if cmd.winecheck():
    print("WINE NOT FOUND")
else:
    print("Wine is good!")

# CLICK STUFF

def on_click():
    userinput = my_entry.get()
    MODE = mode.get()

    inputnonlocal = False

    if MODE == 0:
      userinput = "INPUT/" + userinput
      if userinput == "INPUT/":
       print("You can't use plain folders as an input, this only works in projector rays.")
       return
    if MODE == 1:
      inputnonlocal = True
    
    label.config(text="Button Clicked!")
    print("")
    print(f"User input is {userinput}")
    print("Running Director Extract")
    
    out = cmd.directorextractrun(userinput,inputnonlocal)
    print("--Output--")
    print(out.stdout.strip())
    print("----------")

    # add stuff to extra info

    if out.returncode == 1:
        print("Bad return code! Check Extra Info For Details!")
    else:
       if not out.stderr or out.stderr != "":
        print("Extra info detected!")
    
    consoleA.delete("1.0", tk.END)
    consoleA.insert(tk.END, out.stderr)

def on_clickk():
    userinput = my_entryy.get()
    MODE = modee.get()

    inputnonlocal = False

    if MODE == 0:
        userinput = "INPUT/" + userinput 
    if MODE == 1:
        userinput = "OUTPUT/" + userinput
    if MODE == 2:
        inputnonlocal = True
    
    labell.config(text="Button Clicked!")
    print("")
    print("Running Projector Rays")
    print("This may take a while")
    out = cmd.projectorraysrun(userinput,inputnonlocal)
    print("--Output--")
    print(out.stdout.strip())
    print("----------")

    # add stuff to extra info

    if out.returncode == 1:
        print("Bad return code! Check Extra Info For Details!")
    else:
       if not out.stderr or out.stderr != "":
        print("Extra info detected!")
    
    consoleB.delete("1.0", tk.END)
    consoleB.insert(tk.END, out.stderr)

def show_choice():
    print(f"dfe mode is {mode.get()}")

def show_choicee():
    print(f"pjr mode is {modee.get()}")

root = tk.Tk()
root.title("Henry's Director Experiment GUI")

w, h = 300, 600
x = (root.winfo_screenwidth() - w) // 2
y = 60
root.geometry(f"{w}x{h}+{x}+{y}")

# GUI MAKER

frame = tk.Frame(root)
frame.pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=10, pady=5)

frameb = tk.Frame(root)
frameb.pack()

mode = tk.IntVar()
mode.set(0)

modee = tk.IntVar()
modee.set(0)

# frame 1
label = tk.Label(frame, text="Director Extract", font=("Arial", 15))
label.pack(pady=10)
my_entry = tk.Entry(frame, width=30)
my_entry.pack(pady=10)
tk.Button(frame, text="Run Director Extract", command=on_click).pack()

togA = ToggledFrame(frame, text='Extra Info', relief="raised", borderwidth=1)
consoleA = tk.Text(togA.sub_frame, wrap="word", height=15, width=70)

# frame 2
labell = tk.Label(frameb, text="Projector Rays", font=("Arial", 15))
labell.pack(pady=10)
my_entryy = tk.Entry(frameb, width=30)
my_entryy.pack(pady=10)
tk.Button(frameb, text="Run Projector Rays", command=on_clickk).pack()

togB = ToggledFrame(frameb, text='Extra Info', relief="raised", borderwidth=1)
consoleB = tk.Text(togB.sub_frame, wrap="word", height=15, width=70)

#radio buttons and toggle frames
rb1 = tk.Radiobutton(frame, text="Input Folder", variable=mode, value=0, command=show_choice)
rb2 = tk.Radiobutton(frame, text="Elsewhere (broken)", variable=mode, value=1, command=show_choice)
rb1.pack(anchor="center", padx=0, pady=5)
rb2.pack(anchor="center", padx=0, pady=0)

rb1b = tk.Radiobutton(frameb, text="Input Folder", variable=modee, value=0, command=show_choicee)
rb2b = tk.Radiobutton(frameb, text="Output Folder", variable=modee, value=1, command=show_choicee)
rb3b = tk.Radiobutton(frameb, text="Elsewhere (broken)", variable=modee, value=2, command=show_choicee)
rb1b.pack(anchor="center", padx=0, pady=5)
rb2b.pack(anchor="center", padx=0, pady=0)
rb3b.pack(anchor="center", padx=0, pady=5)

togA.pack(fill="x", expand=0, pady=10, padx=2, anchor="n")
consoleA.pack(padx=10, pady=10)
consoleA.insert("1.0", "Extra info from the director extract output goes here")

togB.pack(fill="x", expand=0, pady=10, padx=2, anchor="n")
consoleB.pack(padx=10, pady=10)
consoleB.insert("1.0", "Extra info from the projectorrays output goes here")

print("Shockwave GUI Start!")

root.mainloop()

