import sys
import socket

def connect_to_server(ip, port):
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((ip, port))

        print(f"Connected to {ip}:{port}")

        # Send data to the server (optional)
        # client_socket.sendall(b"Hello, server!")

        # Receive data from the server (optional)
        # data = client_socket.recv(1024)
        # print("Received:", data.decode())

        # Close the socket
        client_socket.close()

    except ConnectionRefusedError:
        print("Connection refused. Check if the server is running and the IP and port are correct.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python connect.py <server_ip> <server_port>")
    else:
        server_ip = sys.argv[1]
        server_port = int(sys.argv[2])
        connect_to_server(server_ip, server_port)
        
