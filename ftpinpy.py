import ftplib
from ftplib import FTP
server = FTP("192.168.1.58")
server.login()
i = input("Enter File name")+".txt"
file = open(i, "rb")
server.storbinary("STOR "+i, file) # to upload file to server
serverfile = "newhosts.txt" # file present on server
local = open("newfile.txt","ab") # on which we will add server file content
server.retrbinary("RETR "+serverfile, local.write, 1024)
server.quit()
