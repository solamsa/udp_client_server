from socket import *
sever_name = '127.0.0.1'
server_port = 12000
client_socket = socket(AF_INET,SOCK_DGRAM)
message = input('Input lowercase sentence:').encode()
client_socket.sendto(message,(sever_name,server_port))
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message.decode())
# print("from ser")
client_socket.close()