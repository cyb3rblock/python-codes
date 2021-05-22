t = int(input(""))
while t > 0:
    t = t - 1
    n = int(input(""))
    x = []
    for i in range(0,n):
        b = int(input())
        x.append(b)
    a = 0
    for i in range(0,n-1):
        if x[i] == 0 and x[i+1] == 1:
            x[i] = 1
            x[i+1] = 0
            print(x)
            i = i + 1
            a = a + 1
    print("output : " + str(a))
