import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.56.1", 1234))
while True:
    data = input("Enter your message\n")
    s.send(data.encode())
    if data == "quit":
        print("server will break connection now\n")
        break
s.close()