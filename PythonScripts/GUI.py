"""
This script opens a GUI for the read out of the Mean Energy of the laser in 18.1
When pressing the button MeanEnergy it gives back the MeanEnergy and some
additional things (by starting the script MeanEnergy.py) and exit closes the
application.

Date: 09/08/2018
Creator: Manuel Eibl
"""


import tkinter as tk
import os
import importlib as il

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

import MeanEnergy
from MeanEnergy import output
from MeanEnergy import file

def HelloCallBack():
    os.chdir(path)
    #os.system('py MeanEnergy.py')
    il.reload(MeanEnergy)   #reloads the new output value
    from MeanEnergy import output
    s = output +'\n\n'
    file.write(s)
    tex.insert(tk.END, s)
    tex.see(tk.END)     #scrolls if necessary

top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)

tk.Button(bop, text='MeanEnergy', command=HelloCallBack).pack()
tk.Button(bop, text='Exit', command=top.destroy).pack()
top.mainloop()
