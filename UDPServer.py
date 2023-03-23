from socket import *
server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('127.0.0.1', server_port))
print('The server is ready to receive')
while True:
    message, clientAddress = server_socket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    server_socket.sendto(modifiedMessage.encode(), clientAddress)