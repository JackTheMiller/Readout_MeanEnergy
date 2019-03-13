"""
This script is used to read out the mean energy of the laser (door laser, 18.1).
It asks if a new ouput file should be created, opens a GUI which reads the
MeanEnergy whenever the button 'MeanEnergy' is pressed by launching the script
MeanEnergy.py.
Necessary scripts: RunMeanEnergy.py, GUI.py, MeanEnergy.py and Method_YesOrNo.py

Date: 09/08/2018
Creator: Manuel Eibl
"""
import os
import sys
sys.path.append('P:\Python\MeanEnergy\GUI_included\PythonScripts')
import Method_YesOrNo as YoN

path = os.path.dirname(os.path.abspath(__file__))
subdir = '\PythonScripts'
os.chdir(path)

YoN.yes_or_no("Would you like to make a new mean energy file which overwrites the existing one?")

Newpath = os.path.join(path + subdir)
os.chdir(Newpath)

os.system("python GUI.py")
