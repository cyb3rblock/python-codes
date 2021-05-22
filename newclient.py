import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.56.1", 1234))
while True:
    data = input("client: ")
    s.send(data.encode())
    c = s.recv(1024).decode()
    if c == "quit":
        print("server will break connection now\n")
        break
    print("server: " + c)
s.close()