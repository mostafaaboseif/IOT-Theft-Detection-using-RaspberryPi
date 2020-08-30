import socket
from threading import Thread


class SendingThread(Thread):
    def __init__(self, conn): # override Thread's constructor
        Thread.__init__(self)  #
        self.conn = conn  # add the passed connection variable to the private variable of the class

    def run(self):
        # write code to send data continuously
        while True:
            data = input()
            self.conn.send(bytes(data, 'utf-8'))


class ReceivingThread(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn
        self.ret1 = 0
        self.ret2 = 0

    def run(self):
        # write code to receive data continuously
        while True:
            msg = self.conn.recv(1024)
            msg=msg.decode('utf-8')
            # print(msg)
            if msg == 'lightDetected':
                self.ret1 = 1
                # print('1')
            if msg == 'motionDetected':
                self.ret2 = 1
                # print('2')



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
conn1, addr = s.accept()
conn2, addr = s.accept()

receiveThread1 = ReceivingThread(conn1)
# create an another to receive data
receiveThread2 = ReceivingThread(conn2)
# start both threads
receiveThread1.start()
receiveThread2.start()
# receiveThread1.join()
# receiveThread2.join()
while True:
    if (receiveThread2.ret2 == 1) and (receiveThread1.ret1 == 1):
        print("wla3")
        receiveThread1.ret1 = 0
        receiveThread2.ret2 = 0


# with conn:
#     print('Connected by', addr)
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             print('error')
#             break
#         conn.sendall(data)
#         print(data.decode('utf-8'))