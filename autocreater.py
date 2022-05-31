

import sys
import os
""" script will create directory"""
arguments = len(sys.argv)

if arguments <= 1:
    print("Please, provide directories names separated by space")
    sys.exit()
if sys.argv[1] == "--help":
    print("I will create new directories. Please, provide directories names separated by space")
    exit()
if arguments > 1:
    for arg in sys.argv[1:]:
        try:
            str(os.mkdir(arg))
            print("Created directories: " + str(arg))
        except FileExistsError:
            print("Directory " + arg + " " + "already exist")




