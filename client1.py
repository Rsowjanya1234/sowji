import socket
import json


def communicate_with_server(ip, port, sender_name, message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    client.send(sender_name.encode())
    client.send(message.encode())
    response = client.recv(1024).decode()
    client.close()
    return response


with open("ip_port_config.json") as config_file:
    config = json.load(config_file)
    server1_ip = config["server1"]["ip"]
    server1_port = config["server1"]["port"]
    server2_ip = config["server2"]["ip"]
    server2_port = config["server2"]["port"]

while True:
    user_input = input("Enter client message :")
    if user_input.lower() == "exit" or user_input.lower() == "quit":
        break
    recipient_name = input("Enter recipient's name")

    response_server1 = communicate_with_server(server1_ip, server1_port,recipient_name, user_input)
    response_server2 = communicate_with_server(server2_ip, server2_port,recipient_name, user_input)

    print(f"Response from {server1_ip}:{server1_port}: {response_server1}")
    print(f"Response from {server2_ip}:{server2_port}: {response_server2}")

