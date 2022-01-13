# py-socket-server-and-client
An example in Python with a Socket Server and Client to send and receive data to Server. Server support multiple Clients and push messages to all Clients connected.

Make sure you have installed Python on your machine.

First, open terminal and run > python app-server.py
The socket server will running and waiting for client connections.

Open a putty session to connect to server socket host 127.0.0.1 port 14150 Optional, if you want to open more sessions on putty. The server socket is coded to send messages to all client connected.

Open other terminal and run > python app-client.py
Using this client you can type some text and press enter, to send a message to the socket server.

After app-client send the message to the socket server, you'll see on your putty session opened, that the message was recieved (if you opened more than one putty session, you'll see the messages in all sessions).

Enjoy!
It's useful for emulate messages by socket.
