import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.com", 80))

http_get = b"GET / HTTP/1.1\nHost: www.google.com\n\n" # GET Request
data = ''
try:
    sock.sendall(http_get)
    data = sock.recvfrom(1024) # receiving data from the url.
   # print(data)
    strdata = data[0]
    headers = strdata.splitlines() # spliting with space as seperator
    for header in headers:
        print(header.decode())
except socket.error:
    print ("Socket error", socket.error)
finally:
    print("closing connection")
    sock.close()