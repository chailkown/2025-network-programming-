import socket
import time

PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('0.0.0.0', PORT))
    server.listen(5)
    print(f"Time Server running on port {PORT}...")

    while True:
        client_sock, addr = server.accept()
        print(f"Connection from {addr}")
        with client_sock:
            current_time = time.ctime()
            client_sock.sendall(f"Current Time: {current_time}\n".encode())
        print(f"Connection with {addr} closed")
