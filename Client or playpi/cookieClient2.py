import socket
from time import sleep

host = '192.168.1.79' #IP of server (host)
port = 5560  #the same port of the server

def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # This fn connects to the connection established by the server.
    # the server waits for this fn by executing s.accept()
    s.connect((host, port))
    return s

def sendReceive(s, message):
    s.send(str.encode(message))
    reply = s.recv(1024)
    print("We have received a reply")
    print("Send closing message.")
    s.send(str.encode("EXIT"))
    s.close()
    reply = reply.decode('utf-8')
    return reply

def transmit(message):
    s = setupSocket()
    response = sendReceive(s, message)
    return response

