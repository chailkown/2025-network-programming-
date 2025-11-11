import socket
import datetime

class UDPTimeServer:
    def __init__(self, host='0.0.0.0', port=50002, encoding='utf-8'):
        self.host = host
        self.port = port
        self.encoding = encoding

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))
            print(f"[+] UDP TimeServer listening on {self.host}:{self.port}")

            while True:
                data, addr = s.recvfrom(1024)
                print(f"[+] Request from {addr}: {data.decode(self.encoding)}")
                now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
                s.sendto(now.encode(self.encoding), addr)
                print(f"[-] Sent time to {addr}: {now}")


if __name__ == "__main__":
    UDPTimeServer().start()
