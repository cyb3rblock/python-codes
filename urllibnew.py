import urllib.request
u = urllib.request.urlopen("https://raw.githubusercontent.com/logpai/loghub/master/OpenSSH/SSH_2k.log")
f = open("login.txt", "w")
f.close()
for i in u:
    i = i.decode("utf-8")
    l = i.split()
    a = ""
    b = ""
    f = open("login.txt", "r")
    g = f.readlines()
    if l[5] != "Failed":
        continue
    elif l[5] == "Failed" and l[8] == "invalid":
        if len(g) == 0:
            a = l[10]
            b = l[12]
        else:
            count = 0
            for j in g:
                d = j.split()
                if l[10] == d[0] and l[12] == d[1]:
                    count = 1
                    continue
            if count == 0:
                a = l[10]
                b = l[12]
    elif l[5] == "Failed":
        if len(g) == 0:
            a = l[8]
            b = l[10]
        else:
            count = 0
            for j in g:
                d = j.split()
                if l[8] == d[0] and l[10] == d[1]:
                    count = 1
                    continue
            if count == 0:
                a = l[8]
                b = l[10]
    f.close()
    f = open("login.txt","a")
    if a!= "" and b != "":
        f.write(a + " " + b + "\n")
    f.close()
f = open("login.txt","r")
z = f.readlines()
for i in z:
    print(i)
f.close()


