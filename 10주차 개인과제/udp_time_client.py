import socket

class UDPTimeClient:
    def __init__(self, host='172.26.222.117', port=50002, encoding='utf-8'):
        self.host = host
        self.port = port
        self.encoding = encoding

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            message = "REQ_TIME"
            sock.sendto(message.encode(self.encoding), (self.host, self.port))
            print(f"[CLIENT] Request sent to {self.host}:{self.port}")

            data, _ = sock.recvfrom(1024)
            print(f"[CLIENT] Server time: {data.decode(self.encoding)}")

        print("[CLIENT] Connection closed.")


if __name__ == "__main__":
    UDPTimeClient().start()
