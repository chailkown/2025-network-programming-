import socket
import random

PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('0.0.0.0', PORT))
    server.listen(5)
    print(f"Number Server running on port {PORT}...")

    while True:
        client_sock, addr = server.accept()
        print(f"Connection from {addr}")
        with client_sock:
            num = random.randint(1, 100)
            client_sock.sendall(f"Random Number: {num}\n".encode())
        print(f"Connection with {addr} closed")
