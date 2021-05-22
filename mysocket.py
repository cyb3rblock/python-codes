import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
n = input("Enter the IP address\n")
a = int(input("Enter starting port\n"))
b = int(input("Enter the Ending port\n"))
for i in range(a,b+1):
    l = (n,i)
    x = sock.connect_ex(l)
    sock.settimeout(5)
    if x == 0:
        print(i,"  open")
    else:
        print(i,"  close")
sock.close()