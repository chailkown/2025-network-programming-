import socket
import datetime

class TimeServer:
    def __init__(self, host='0.0.0.0', port=50001, encoding='utf-8'):
        self.host = host
        self.port = port
        self.encoding = encoding

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # 포트 재사용 설정
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(5)
            print(f"[+] TimeServer listening on {self.host}:{self.port}")

            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"[+] Connected: {addr}")
                    self.handle_client(conn, addr)
                    print(f"[-] Disconnected: {addr}")

    def handle_client(self, conn, addr):
        """현재 시각을 ISO 형식으로 전송"""
        now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        msg = f"{now}\n"
        conn.sendall(msg.encode(self.encoding))


if __name__ == "__main__":
    TimeServer().start()
