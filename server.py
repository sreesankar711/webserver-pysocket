from socket import *

sPort = 4000
sSocket = socket(AF_INET, SOCK_STREAM)
ADDR = ('localhost', sPort)
sSocket.bind(ADDR)

sSocket.listen(1)
print("The server is listening on ",ADDR)

while True:
    cSocket, addr = sSocket.accept()
    print("connected with ",addr)
    message = cSocket.recv(1024).decode()
    if message:
        filename = message.split()[1][1:]

        try:
            with open(filename) as f:
                outputData = f.read().encode()
                responseMessage = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: " + str(len(outputData)).encode() + b"\r\n\r\n" + outputData
        except FileNotFoundError:
            outputData = b"<html><body><h1>404 Not Found</h1></body></html>"
            responseMessage = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: " + str(len(outputData)).encode() + b"\r\n\r\n" + outputData

        cSocket.send(responseMessage)
        print("connection closed with ",addr)
        cSocket.close()
    else:
        print("no message by ",addr)
        cSocket.close()
