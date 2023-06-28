import sys
import socket

def connect_to_ip(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        print("Connected to {}:{}".format(ip, port))
        # Perform further actions as needed
        sock.close()
    except ConnectionRefusedError:
        print("Connection refused to {}:{}".format(ip, port))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python connect.py <ip> <port>")
    else:
        ip = sys.argv[1]
        port = int(sys.argv[2])
        connect_to_ip(ip, port)

