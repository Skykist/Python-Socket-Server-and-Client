import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.0.7"
port = 9500

sock.connect((server,port))

"""sock.send("hey, hi, hello".encode())
message = sock.recv(1024)

print(message)"""

sock.send("Hello".encode())
message = sock.recv(1024)

print(message)
