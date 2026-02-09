# server.py
import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on port {PORT}...")

conn, addr = server.accept()
print("Connected by:", addr)

data = conn.recv(1024)
print("Received:", data.decode())

conn.sendall(b"Hello from server")
conn.close()
