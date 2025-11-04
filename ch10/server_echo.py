import socket

BUF_SIZE = 128
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('0.0.0.0', PORT))
    server.listen(5)
    print(f"Echo Server running on port {PORT}...")

    while True:
        client_sock, addr = server.accept()
        print(f"Connection from {addr}")
        with client_sock:
            while True:
                data = client_sock.recv(BUF_SIZE)
                if not data:
                    break
                print(f"Received: {data.decode().strip()}")
                client_sock.sendall(data)
        print(f"Connection with {addr} closed")
