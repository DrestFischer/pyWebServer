#import socket module
from socket import *

#Prepare TCP sever socket
#(AF_INT Address Family for IPv4 protocols)
#(SOCK_STREAM for TCP, SOCK = socket kind)
serverSocket = socket(AF_INET, SOCK_STREAM)

#Assign a port number
serverPort = 12000

#Bind the socket to the server address and server port
serverSocket.bind(('', serverPort))

#Listen to at most 1 connection at a time
serverSocket.listen(1)

#Create True statement
while True:

    #Output to screen confirming server established and ready for connection
    print('Ready to serve...')

    #Create acceptance of client connection
    connectionSocket, addr =  serverSocket.accept() #Done

    #Limited deployment of try
    #Receive client connection, respond with HTTP header to confirm open connection
    #Correct file requested, delivered to client
    #Incorrect file request, move to Except clause
    try:
        #Set receive message from client (maximum 1024 bytes)
         thmessage = connectionSocket.recv(1024)

        #Split the message to identify the file name only - using the all after / [1]
        filename = message.split()[1]

        #Open the requested file
        f = open(filename[1:])

        #Read the file into variable
        outputdata = f.read()

        #Send HTTP header to client
        #Code 200 = OK
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")

        #Encode and send the file, via variable outputdata
        for i in range(0, len(outputdata)):
            	connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        #Close client connection socket
        connectionSocket.close()

    #Where exact file doesn't exist the IOError will be triggered
    except IOError:
        #Send HTTP 404 header and message
        connectionSocket.send(b"HTTP/1.1 404 Not found\r\n\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not found</h1></body></html>")


        #Close client connection socket
        connectionSocket.close()

#Close server socket
serverSocket.close()

#Terminate program and exit
sys.exit()
