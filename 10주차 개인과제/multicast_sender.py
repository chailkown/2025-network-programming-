import socket
import struct
import time
import datetime

class UDPMulticastSender:
    def __init__(self, group_ip='224.1.1.1', port=5007, ttl=1, encoding='utf-8'):
        self.group_ip = group_ip
        self.port = port
        self.ttl = ttl
        self.encoding = encoding

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        ttl_bin = struct.pack('b', self.ttl)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl_bin)
        print(f"[+] Multicast sender started on {self.group_ip}:{self.port}")

        try:
            while True:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                msg = f"[{now}] 멀티캐스트 테스트 메시지"
                sock.sendto(msg.encode(self.encoding), (self.group_ip, self.port))
                print(f"[+] Sent: {msg}")
                time.sleep(3)
        except KeyboardInterrupt:
            print("\n[-] 송신 종료")
        finally:
            sock.close()

if __name__ == "__main__":
    UDPMulticastSender().start()
