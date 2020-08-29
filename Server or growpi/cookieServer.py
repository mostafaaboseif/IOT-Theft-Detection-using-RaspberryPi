import socket

host = ''  #the host is the pi itself, we are the server
port = 5560  #large nb to avoid reserved ports

storedValue = "Yo, what's up?"

def setupServer():
    # AF: address family , INET: IPv4 addresses 
    # SOCK_STREAM: TCP Connection
    # this fn creates a socket (connection between server & client)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    # we added try except to indicate if there is any errors
    # this fn binds (connects) the host (IP address) 
    # & port (exact room of communication) to the created socket
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    # puts the server into listening mode, waits for ONE connection
    s.listen(1)
    # after listening, the server accepts a connection.
    # the fn returns a connection object (to be used) and {IP address, port}
    # this is a blocking fn, it won't continue unless a connection is accepted
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data, 1024 is the received buffer size
        # we receive the command first as a server to specify 
        # the service we need to provide to the client
        data = conn.recv(1024)
        # data is received in bytes, so we need to decode it to string
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Our client has left us :(")
            break
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
            break
        else:
            reply = 'Unknown Command'
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    # close the connection if we break from the loop
    conn.close()
        

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break
