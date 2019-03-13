"""
This Method defines the function yes_or_no which.
This is used in the RunMeanEnergy.py script to ask the user if a new
.txt file should be created at the start for its output values or not.
If not, the output values are appended to the existing file.

Date: 31.07.2018
Creator: Manuel Eibl
"""
import sys

def yes_or_no(question, default='no'):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    yes = ['yes', 'y', 'ye']
    no = ['no', 'n']
    if default is None:
        prompt = ' [y/n] '
    elif default == "yes":
        prompt = ' [y/n] '
    elif default == 'no':
        prompt = ' [y/n] '
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    sys.stdout.write(question + prompt)
    choice = input().lower()
    if choice in yes:
        file = open("MeanEnergy.txt", "w+")
        print('A new file was created succesfully')
    elif choice in no:
        print('The data will be appended to the existing file.')
    else:
        sys.stdout.write("Please respond with 'yes' or 'no' "
                         "(or 'y' or 'n').\n")
