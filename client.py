from socket import *

sPort = 4000
cSocket = socket(AF_INET, SOCK_STREAM)
ADDR = ('localhost', sPort)

cSocket.connect(ADDR)
print("Cient connected with ",ADDR)

filename = input("Enter the file name: ")
request = "GET /" + filename + " HTTP/1.1\r\nHost: localhost\r\n\r\n"
cSocket.send(request.encode())

response = cSocket.recv(1024).decode()
print(response)

cSocket.close()