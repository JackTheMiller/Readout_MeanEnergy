"""
This script reads out the mean laser energy written by the power meter (1918-R)
software into its standard path.
___
Input:
Takes the file which is produced when pressing Get data in the tools section of
the power meter software.
___
Output:
Gives Mean energy value in uJ of the chosen accumulations and the Accumulations
(e.g. 100).
The output is printed into the GUI window (generated in the script GUI.py)
as well as in an output file named MeanEnergy.txt

Date: 31/07/2018
Creator: Manuel Eibl
"""
import os
import numpy as np
import datetime

# Path of ouput file of power meter software
Parentpath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
os.chdir(Parentpath)
file = open('MeanEnergy.txt', 'a+')
#path = 'C:/Program Files/Newport/Newport Power Meter Application/Bin'
#path = os.path.dirname(os.path.abspath(__file__))
#os.chdir(path)

FNAME = 'DataStore.txt'
data = []
Accdata = np.genfromtxt(FNAME, dtype=float, skip_header = 14, skip_footer = 1)
with open(FNAME) as fp:
    for (i, line) in enumerate(fp):
        if i == 0:
            # 1st line
            output = 'Time: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            #print()
            #print('Time: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            #print()
            output += '\nAccumulations: ' + line
            #print('Accumulations: ' + line)
            #file.write('Time: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            #file.write('\n')
            #file.write('Accumulations: ' + line)
        elif i > 0:
            break
mean = np.sum(Accdata)/len(Accdata)
output += 'Mean energy: ' + str(round(mean*1E6, 2)) + ' uJ'
output += '\n' + str(np.sum(Accdata)) +'\n'+ str(len(Accdata))
print(output)
#print('Mean energy: ' + str(round(mean*1E6, 2)) + ' um')
#print()
#file.write('Mean energy: ' + str(round(mean*1E6, 2)) + ' um')
#file.write('\n')
#file.write('\n')
#file.write('\n')
