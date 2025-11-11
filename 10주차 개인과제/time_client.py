import socket

class TimeClient:
    def __init__(self, host='172.26.222.117', port=50001, encoding='utf-8'):
        self.host = host
        self.port = port
        self.encoding = encoding

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            print(f"[CLIENT] Connected to {self.host}:{self.port}")

            data = sock.recv(1024)
            print(f"[CLIENT] Server time: {data.decode(self.encoding)}")

        print("[CLIENT] Connection closed.")


if __name__ == "__main__":
    TimeClient().start()
