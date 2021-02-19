import os
from imp import find_module
import sys

missing = None
onefile = None

try:
    find_module('pyinstaller')
except ImportError:
    missing = True

if missing:
    print("Error: pyinstaller not found, please install pyinstaller - if you get an error while installing, try installing with administrator permissions")
    sys.exit()

while onefile == None:
    yn = input("Do you want the program to be ran in one file? (Y/N) ")

    if yn.lower() == "y":
        onefile = True
    elif yn.lower() == "n":
        onefile = False

try:
    if onefile:
        os.system("pyinstaller client.py --onefile")
        print("client.py compiled, can be found in dist directory")
    else:
        os.system("pyinstaller client.py")
        print("client.py compiled, can be found in dist directory")

except FileNotFoundError:
    print("File client.py has not been found")
