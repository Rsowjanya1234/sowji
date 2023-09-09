import socket
import threading
import json

def handle_client(client_socket):
    recipient_name = client_socket.recv(1024).decode()
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"server1 received: {data} for {recipient_name}")
        recipient_ip = data_json["servers"][recipient_name]
        recipient_port = data_json["ports"][data_json["servers"].index(recipient_ip)]
        recipient_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        recipient_socket.connect((recipient_ip,recipient_port))
        recipient_socket.send(data.encode())
        recipient_socket.close()
        #client_socket.send(data.encode())
    client_socket.close()

def start_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((ip, port))
        server.listen(5)
        print(f'server1 listening on {ip}:{port}')
        while True:
            client_socket, client_address = server.accept()
            print(f"connected to servers - port number{port}")

            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except OSError as e:
        print(f"Error: {e}")
    finally:
        server.close()


if __name__ == "__main__":
    with open("data.json",'r') as config_file:
        config = json.load(config_file)
   server_name = "Srisindhu"
   servers = config["servers"]
   servers_ip = servers[server_name]
   server1_port = servers["port"]
   start_server(server1_ip, server1_port)

