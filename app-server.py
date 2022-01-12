import socket
import os
import threading
from threading import Thread
import _thread

clients = set()
clients_lock = threading.Lock()

def listener(client, address):
    print ("Accepted connection from: ", address)
    with clients_lock:
        clients.add(client)
    try:    
        while True:
            data = client.recv(1024)
            if not data:
                break
            else:
                print (repr(data))
                with clients_lock:
                    for c in clients:
                        c.sendall(data)
    finally:
        with clients_lock:
            clients.remove(client)
            client.close()

host = ''
port = 14150

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(3)
th = []

while True:
    print ("Server is listening for connections...")
    client, address = s.accept()
    th.append(Thread(target=listener, args = (client,address)).start())

s.close()