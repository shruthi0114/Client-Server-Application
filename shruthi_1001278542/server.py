import socket
from thread import *
import string

# socket connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8889))
s.listen(10)
c = {}

global client#sender list
client=[]
global client1#receipient list
client1=[]
global flag
flag=' '
def clientthread(conn):
    a=1
    while a:
        data = conn.recv(1024)
        e = data.split('>')

        if len(e) == 3:
            # indicates receiver is ready to receive messages
            if e[1] == 'show':
                client1.append(e[0])
                client.append(e[2])
                try:
                    m = ''
                    for i in range(0, len(c[e[0]])):
                        m = m + c[e[0]][i]
                        if i != (len(c[e[0]])-1):
                            m = m + '\n'
                        if m == '':
                            data = 'No incoming messages' # client has no message to receive
                        else:
                            data1=m
                            print m
                            d=data1.split('$')
                            d1=d[0].split('>')
                            data=d1[0] +">"+d[1]



                    del c[e[0]]
                except:
                    data = 'No messages'
            # Client wants to send message
            else:
                try:
                    c[e[1]]
                except:
                    c[e[1]] = []
                if e[1] in client1:
                    i=client1.index(e[1])
                    if e[0] == client[i]:
                        c[e[1]].append(e[0] + '>' + e[2])
                        client.append(e[0])
                        client1.append(e[1])
                        data = 'sent'
                    # If client tries to connect to already connected users
                    else:
                        c[e[1]]=' '
                        data = 'User Busy. Message not sent'

                else:
                    c[e[1]].append(e[0] + '>' + e[2])
                    client.append(e[0])
                    client1.append(e[1])
                    data="sent"
        else:
            data = 'Error'
        conn.send(data)
    conn.close()
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread ,(conn,))
s.close()
