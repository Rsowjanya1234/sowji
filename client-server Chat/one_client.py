import socket
import json

with open('server_config.json') as config_file:
    config = json.load(config_file)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (config['ip'], config['port'])
client_socket.connect(server_address)

while True:
    message = input("Client: ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'exit':
        print("Connection closed by client.")
        break
    response = client_socket.recv(1024).decode('utf-8')
    print("Server:", response)
  
client_socket.close()
