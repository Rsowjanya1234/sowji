import socket
import json

def handle_client(client_socket,client_address):
    print("Connected to", client_address)

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        
        if not data:
          break
        print("Client:", data)
        
        if data.lower() == 'exit':
            print("Connection closed by client.")
            break
            
        response = input("Server: ")
        client_socket.send(response.encode('utf-8'))
    print("Connection closed for", client_address)
    client_socket.close()
    
with open('server_config.json') as config_file:
      config = json.load(config_file)
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (config['ip'], config['port'])
server_socket.bind(server_address)
server_socket.listen(1)
print("Waiting for a connection...")
while True:
    client_socket, client_address = server_socket.accept()
    handle_client(client_socket, client_address)
