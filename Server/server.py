import socket
from threading import Thread
from twython import Twython

consumer_key = 'uie5XwgqJGSezcbOV75bO2Yv7'
consumer_secret = 'zVhFCxE2GXOwUYnfB7pud0jL5qdJuW8w1aJKx8oGw6dbch26q1'
access_token = '1579568184-4zIVgRoHEbpCtvKAgpc3RRkppz04tGXNPIAOqAt'
access_token_secret = 'QLEg7ala0nxZ19r8TSoKZ3zU9GcqMxcK9rhPivw9MmfRX'


twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
host = ''
port = 5560


def tweetImage(img, message):
    photo = open(img, 'rb')
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=message, media_ids=[response['media_id']])
    print("Tweeted: %s" % message)

def storeFile(filePath, conn):
    picFile = open('D:/cookieImages/thief.jpg', 'wb')
    print("Opened the file.")
    pic = conn.recv(1024)
    while pic:
        print("Receiving picture still.")
        picFile.write(pic)
        pic = conn.recv(1024)
    picFile.close()

class ReceivingThread(Thread):
    def __init__(self, conn, client):
        Thread.__init__(self)
        self.conn = conn
        self.client = client

    def run(self):
        while True:
            if self.client == "light":
                # print("Light Detected")
                msg = self.conn.recv(1024)
                msg = msg.decode('utf-8')
                print(msg)
                tweetImage("D:/cookieImages/light.jpg", "THIEF DETECTED!!!!!!!!!!")
                self.client = ""

            elif self.client == "motion":
                print("Motion Detected")
                # msg = self.conn.recv(1024)
                # msg = msg.decode('utf-8')
                # print(msg)
                imageData = self.conn.recv(1024)  # receive the data
                imageData = imageData.decode('utf-8')
                print("received in data transfer")
                # Split the data such that you separate the command
                # from the rest of the data.
                dataMessage = imageData.split(' ', 1)
                command = dataMessage[0]
                print("received in data transfer2")
                if command == 'STORE':
                    print("Store command received. Time to save a picture")
                    storeFile(dataMessage[1], self.conn)
                    tweetImage("D:/cookieImages/thief.jpg", "This is the thief")
                    print("File stored.")
                else:
                    print('Unknown Command')
                self.conn.close()
                print("Motion Detector End")
                self.client = ""


def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1)  # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        imageData = conn.recv(1024)  # receive the data
        imageData = imageData.decode('utf-8')
        print("received in data transfer")
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = imageData.split(' ', 1)
        command = dataMessage[0]
        print("received in data transfer2")
        if command == 'STORE':
            print("Store command received. Time to save a picture")
            storeFile(dataMessage[1],conn)
            reply = "File stored."
            break
        elif command == 'EXIT':
            print("Our client has left us :(")
            break
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
            break
        else:
            print('Unknown Command')
        print("received in data transfer3")
    conn.close()


s = setupServer()

s.listen(1)
print("Waiting For Threads To Connect")
conn1, addr = s.accept()
print("Light Thread Connected")
conn2, addr = s.accept()
print("Motion Thread Connected")
# create an another to receive data

lightThread = ReceivingThread(conn1, "light")
motionThread = ReceivingThread(conn2, "motion")

lightThread.start()
motionThread.start()

print("Threads Started")
# lightThread.join()
# motionThread.join()

while True:
    pass
    # print("Motion Detected")
    # # msg = self.conn.recv(1024)
    # # msg = msg.decode('utf-8')
    # # print(msg)
    # imageData = conn2.recv(1024)  # receive the data
    # imageData = imageData.decode('utf-8')
    # print("received in data transfer")
    # # Split the data such that you separate the command
    # # from the rest of the data.
    # dataMessage = imageData.split(' ', 1)
    # command = dataMessage[0]
    # print("received in data transfer2")
    # if command == 'STORE':
    #     print("Store command received. Time to save a picture")
    #     storeFile(dataMessage[1], conn2)
    #     reply = "File stored."
    #     break
    # else:
    #     print('Unknown Command')
    # conn2.close()
    # print('Allah')
    # print("Motion Detector End")



# import socket
# from threading import Thread
#
#
# class SendingThread(Thread):
#     def __init__(self, conn): # override Thread's constructor
#         Thread.__init__(self)  #
#         self.conn = conn  # add the passed connection variable to the private variable of the class
#
#     def run(self):
#         # write code to send data continuously
#         while True:
#             data = input()
#             self.conn.send(bytes(data, 'utf-8'))
#
#
# class ReceivingThread(Thread):
#     def __init__(self, conn):
#         Thread.__init__(self)
#         self.conn = conn
#         self.ret1 = 0
#         self.ret2 = 0
#
#     def run(self):
#         # write code to receive data continuously
#         while True:
#             msg = self.conn.recv(1024)
#             msg=msg.decode('utf-8')
#             print(msg)
#             if msg == 'light Detected':
#                 self.ret1 = 1
#                 print('1')
#             if msg == 'motion Detected':
#                 self.ret2 = 1
#                 print('2')
#
#
# HOST = ''  # Standard loopback interface address (localhost)
# PORT = 5560        # Port to listen on (non-privileged ports are > 1023)
#
# s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(2)
# print("Hereee")
# conn1, addr = s.accept()
# print("Threreee")
# conn2, addr = s.accept()
# print("Henaaak")
# receiveThread1 = ReceivingThread(conn1)
# # create an another to receive data
# receiveThread2 = ReceivingThread(conn2)
# # start both threads
# receiveThread1.start()
# receiveThread2.start()
#
# while True:
#     if (receiveThread1.ret2 == 1) and (receiveThread2.ret1 == 1):
#         print("wla3")
#         receiveThread2.ret1 = 0
#         receiveThread1.ret2 = 0
#
#
# import socket
# # from cookieLED import callLED
#
# host = ''
# port = 5560
#
#
# def setupServer():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Socket created.")
#     try:
#         s.bind((host, port))
#     except socket.error as msg:
#         print(msg)
#     print("Socket bind comlete.")
#     return s
#
#
# def setupConnection():
#     s.listen(1)  # Allows one connection at a time.
#     conn, address = s.accept()
#     print("Connected to: " + address[0] + ":" + str(address[1]))
#     return conn
#
#
# def storeFile(filePath):
#     picFile = open('C:/Users/moham/Downloads/IOT-Theft-Detection-using-RaspberryPi-master/mostafa.jpg', 'wb')
#     print("Opened the file.")
#     pic = conn.recv(1024)
#     while pic:
#         print("Receiving picture still.")
#         picFile.write(pic)
#         pic = conn.recv(1024)
#     picFile.close()
#
#
# def dataTransfer(conn):
#     # A big loop that sends/receives data until told not to.
#     while True:
#         # Receive the data
#         data = conn.recv(1024)  # receive the data
#         data = data.decode('utf-8')
#         # Split the data such that you separate the command
#         # from the rest of the data.
#         dataMessage = data.split(' ', 1)
#         command = dataMessage[0]
#         if command == 'STORE':
#             print("Store command received. Time to save a picture")
#             storeFile(dataMessage[1])
#             reply = "File stored."
#             break
#         elif command == 'EXIT':
#             print("Our client has left us :(")
#             break
#         elif command == 'KILL':
#             print("Our server is shutting down.")
#             s.close()
#             break
#         else:
#             reply = 'Unknown Command'
#     conn.close()
#
#
# s = setupServer()
# conn = setupConnection()
# dataTransfer(conn)
#
# print("Picture transfer completed")
#
