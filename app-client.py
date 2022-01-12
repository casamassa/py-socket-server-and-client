#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 14150  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        value = input("Please enter a string (Press Ctrl+c to exit):\n")
        print(f'You entered {value}')
        s.sendall(str.encode(value + "\n"))
        data = s.recv(1024)

        print("Received", repr(data))