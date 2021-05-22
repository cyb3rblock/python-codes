import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.56.1", 1234))
s.listen(2)
conn, addr = s.accept()  # output for s.accept will be nested tuple as one is onject other is addr
print("client addr", addr)
while True:
    data = conn.recv(1024)
    print("client: " + data.decode())
    x = input("server: ")
    conn.send(x.encode())
    if x == "quit":
        print("ending session")
        s.close()
        break
