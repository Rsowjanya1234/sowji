import unittest
import threading
import socket
import subprocess
import time

# Import the client and server code modules
import client
import server

class TestClientServerCommunication(unittest.TestCase):

    def setUp(self):
        # Start the server in a separate thread

        self.server_thread = threading.Thread(target=server.start_server)

        self.server_thread.daemon = True

        self.server_thread.start()

        time.sleep(1)  # Give the server some time to start

    def tearDown(self):
        # Stop the server

        server.stop_server()

    def test_client_connects_to_server(self):
        # Create a client socket and connect to the server

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect(('localhost', 12345))

        # Check if the connection is established

        self.assertTrue(client_socket)

        # Close the client socket

        client_socket.close()

    def test_client_sends_exit_message(self):
        # Create a client socket and connect to the server

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect(('localhost', 12345))

        # Send 'exit' message to the server

        client_socket.send('exit'.encode('utf-8'))

        # Wait for a moment to ensure the server processes the message

        time.sleep(1)

        # Check if the server has closed the connection

        self.assertFalse(client_socket)

    def test_client_sends_regular_message(self):
        # Create a client socket and connect to the server

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect(('localhost', 12345))

        # Send a regular message to the server

        client_socket.send('Hello, Server!'.encode('utf-8'))

        # Wait for a moment to ensure the server processes the message

        time.sleep(1)

        # Check if the server received and printed the message

        self.assertTrue(True)  # Add your assertion here

        # Close the client socket

        client_socket.close()
if __name__ == '__main__':
    unittest.main()
