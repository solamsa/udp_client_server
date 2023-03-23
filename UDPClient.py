from socket import *
sever_name = 'hostname'
server_port = 12000
client_socket = socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentence:')
client_socket.sendto(message,(sever_name,server_port))
modified_message, server_address = client_socket.recvfrom(2048)
print(modified_message)
print("from ser")
client_socket.close()