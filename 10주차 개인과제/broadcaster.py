import socket
import time

BROADCAST_IP = "255.255.255.255"  # 모든 장치에게 전송
PORT = 5005
ENC = "utf-8"

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print(f"[+] Broadcasting messages to {BROADCAST_IP}:{PORT}")

try:
    while True:
        msg = input("메시지를 입력하세요 (exit 입력 시 종료): ")
        if msg.lower() == "exit":
            break
        sock.sendto(msg.encode(ENC), (BROADCAST_IP, PORT))
        print("[+] 메시지 전송 완료")
        time.sleep(1)
finally:
    sock.close()
