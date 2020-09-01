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
                print("Light Detected")
                msg = self.conn.recv(1024)
                msg = msg.decode('utf-8')
                print(msg)
                tweetImage("D:/cookieImages/light.jpg", "THIEF DETECTED!!!!!!!!!!")
                self.client = ""

            elif self.client == "motion":
                print("Motion Detected")
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

s = setupServer()

s.listen(1) # s.listen(2)
print("Waiting For Threads To Connect")
connLight, addr = s.accept()
print("Light Thread Connected")
connMotion, addr = s.accept()
print("Motion Thread Connected")
# create an another to receive data

lightThread = ReceivingThread(connLight, "light")
motionThread = ReceivingThread(connMotion, "motion")

lightThread.start()
motionThread.start()

print("Threads Started")

while True:
    pass
