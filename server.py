import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.0.7"
port = 9500

sock.bind((server,port))
print(sock)

sock.listen(5)
print("ther server is listening...\n")

while True:
    c, addr = sock.accept()
    print("Connection established")

    message = c.recv(1024).decode()
    print("Message received")
    
    if message == "Hello":
        c.send("Hi".encode())
    else:
        c.send("Goodbye".encode())

    print("Response sent")

c.close()
sock.close()
