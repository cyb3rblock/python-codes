n = input("Enter your name and i will give your b'day\n")
f = open("bday.txt")
l = f.readlines()
print("Database right now\n")
for i in l:
    print(i)
f.close()
flag = 0
for i in l:
    a = i.split()
    if a[0] == n:
        print("your bday is %s" % a[1] + " %s" % a[2])
        flag = 1
        break
if flag == 0:
    f = open("bday.txt", "a")
    a = input("Sorry i don't have your info please enter your b'day i will save it\n")
    f.write(n + " " + a + "\n")
    f.close()
    print("Have added your b'day")
    f = open("bday.txt", "r")
    x = f.readlines()
    print("Updated database\n")
    for i in x:
        print(i)
    f.close()