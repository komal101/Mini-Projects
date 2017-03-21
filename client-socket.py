import socket
import time
#import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 4455

count = 0

print("Client: Trying to connect...")

while count == 0:
    try:
        # Client initiates the connection to the server ip and port
        s.connect(('localhost',port))
        count += 1
    except:
        pass

print("Client: Connection Establised!")
while True:

    # Once connected, client allows data to be Received no more than given bytes in its buffer
    msg = s.recv(4000).decode('ascii') # 4000 is no. of bytes of data allowed to be received in the buffer

    print(msg)
    while msg != 'Ok bye': # 'Ok bye' is a message sent by the server
        client_response = input()

        s.send(client_response.encode('ascii'))
        msg = s.recv(4000).decode('ascii')

        print(msg)

    s.close()

    break

