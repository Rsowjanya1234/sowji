import socket
import json

#open and read the server configuration from 'server_config.json'
with open('server_config.json') as config_file:
    config = json.load(config_file)
    
#create a client socket an connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (config['ip'], config['port'])
client_socket.connect(server_address)

while True:
    message = input("Client: ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'exit':
        print("Connection closed by client.")
        break
    #Receive and display the servers response
    response = client_socket.recv(1024).decode('utf-8')
    print("Server:", response)
    
#Close the client socket when done  
client_socket.close()
