import time

import sys

import socket

import os



s = socket.socket()

host = "oshio"

port = 8080

s.connect((host, port))

print("")

print(" Connected to server ")



command = s.recv(1024)

command = command.decode()

if command == "shutdown":

    print("")

    print("Shutdown command")

    s.send("Command recieved".encode())

    os.system("shut.bat")





