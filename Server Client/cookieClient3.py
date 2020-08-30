import socket
from time import sleep
from time import time

host = '127.0.0.1'
port = 5560

def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendPic(s, filePath):
    print(filePath)
    pic = open(filePath, 'rb')
    chunk = pic.read(1024)
    s.send(str.encode("STORE " + filePath))
    t = time()
    while chunk:
        print("Sending Picture")
        s.send(chunk)
        chunk = pic.read(1024)
    pic.close()
    print("Done sending")
    print("Elapsed time = " + str(time() - t) + 's')
    s.close()
    return "Done sending"

def backup(filePath):
    s = setupSocket()
    response = sendPic(s, filePath)
    return response

print(backup('C:/Users/moham/Downloads/IOT-Theft-Detection-using-RaspberryPi-master/ay7aga2.jpg'))


