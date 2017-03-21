# create an INET (IPV4), STREAMing(TCP) socket
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host or a localhost, and a well-known port or system ports
# '' is for local address i.e within a network and socket.gethostname() is used for public host
s.bind(('', 4455)) # double brackets cuz .connect takes only one arguement
# accepts up to 5 requests
s.listen(5)

print("Server: Waiting for a Connection")

while True:
    # accept connections from outside
    # clientsocket is the client's port number and address is clien'ts public ip address
    (clientsocket, address) = s.accept()
    print("client "+address[0]+" has connected to " + str(s))

    msg='Server: Thank you Client for connecting to me. How May I help You?'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))

    result = clientsocket.recv(1024).decode('ascii')
    print(result)
    while result != 'quit': # 'quit' is the message sent by the client

        msg1 = 'Anything else?'
        clientsocket.send(msg1.encode('ascii'))
        result = clientsocket.recv(1024).decode('ascii')
        print(result)

    bye = 'Ok bye'
    clientsocket.send(bye.encode('ascii'))
    clientsocket.close()

    break
