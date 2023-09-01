import socket 
import threading 
import json 


def handle_client(client_socket): 
    while True: 
        data = client_socket.recv(1024).decode() 
        if not data: 
            break 
        print(f"server1 received: {data}") 
        client_socket.send(data.encode()) 
    client_socket.close() 


def start_server(ip, port): 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try: 
        server.bind((ip, port)) 
        server.listen(5) 
        print(f"server1 listening on {ip}:{port}") 

        while True: 
            client_socket, client_address = server.accept() 
            print(f"connected to server1 - port number{port}") 

            client_thread = threading.Thread(target=handle_client, args=(client_socket,)) 
            client_thread.start() 
    except OSError as e: 
        print(f"Error: {e}") 
    finally: 
        server.close() 


if __name__ == "__main__": 
    with open("ip_port_config.json") as config_file: 
        config = json.load(config_file) 

        server1_ip = config["server1"]["ip"] 
        server1_port = config["server1"]["port"] 

    start_server(server1_ip, server1_port) 

