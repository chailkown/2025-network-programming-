import socket
import sys

BUF_SIZE = 128

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <ServerIP> <Port>")
    sys.exit(1)

server_ip = sys.argv[1]
server_port = int(sys.argv[2])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")
    except Exception as e:
        print(f"Connection failed: {e}")
        sys.exit(1)

    try:
        while True:
            msg = input("Message to send (Enter to quit): ")
            if not msg:
                break
            s.sendall(msg.encode())
            data = s.recv(BUF_SIZE)
            if not data:
                print("Server closed connection.")
                break
            print("From server:", data.decode().strip())
    except KeyboardInterrupt:
        print("\nClient exiting.")
