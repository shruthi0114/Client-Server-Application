import socket, Queue
from os import kill
from thread import *
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8889))
# Username Login
u = raw_input('Username: ')

print 'Enter recipient name'
rec = raw_input()
#print type(rec)
print 'Enter message'


client1 =[]
client1.append(rec)

# Sending messages to the Server
def sending(s):

    while 1:
            # Adding HTTP Headers to the message
            msg=  "GET / HTTP/1.1\r\n\r\n $"+raw_input()

            rec2=rec+'>'+msg

            s.send(u + '>' + rec2)
            print s.recv(1024)

# Receiving messages from the server
def receiving(s):
    a='True'
    while a:

        s.send(u + '>show>' +rec)
        r = s.recv(1024)
        if r != 'No messages' and r != 'Disconnect':
            print r
        elif r == 'Disconnect':
            print 'Conncetion Disconnected'



start_new_thread(receiving ,(s,))

start_new_thread(sending ,(s,))
while 1:
    pass
