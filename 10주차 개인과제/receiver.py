import socket

PORT = 5005
ENC = "utf-8"

# UDP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", PORT))  # 모든 네트워크 인터페이스에서 수신 허용

print(f"[+] Listening for broadcast messages on port {PORT}...")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"[Message from {addr[0]}]: {data.decode(ENC)}")
except KeyboardInterrupt:
    print("\n[-] 수신 종료")
finally:
    sock.close()
