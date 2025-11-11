import socket
import struct

class UDPMulticastReceiver:
    def __init__(self, group_ip='224.1.1.1', port=5007, encoding='utf-8'):
        self.group_ip = group_ip
        self.port = port
        self.encoding = encoding

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', self.port))  # 모든 인터페이스에서 수신

        # 멀티캐스트 그룹 가입
        group = socket.inet_aton(self.group_ip)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        print(f"[+] Joined multicast group {self.group_ip}:{self.port}")
        print("[+] Listening for multicast messages...\n")

        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(f"[{addr[0]}] {data.decode(self.encoding)}")
        except KeyboardInterrupt:
            print("\n[-] 수신 종료")
        finally:
            sock.close()

if __name__ == "__main__":
    UDPMulticastReceiver().listen()
