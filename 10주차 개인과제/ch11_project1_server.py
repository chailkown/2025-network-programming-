import socket, datetime

HOST, PORT = "0.0.0.0", 50001
ENC = "utf-8"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(100)
    print(f"[+] TimeServer listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[+] Connected: {addr}")
            now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
            msg = f"{now}\n"
            conn.sendall(msg.encode(ENC))
            print(f"[-] Disconnected: {addr}")