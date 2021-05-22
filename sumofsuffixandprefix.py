def prefix(e, i):
    sum = 0
    for j in range(0, i + 1):
        sum = sum + e[j]
    return sum


def suffix(e, i):
    sum = 0
    for j in range(i, len(e)):
        sum = e[j] + sum
    return sum


t = int(input(""))
while t > 0:
    t = t - 1
    n = int(input("\n"))
    j = 0
    x = []
    for j in range(0, n):
        a = int(input("\n"))
        x.append(a)
    b = []
    for i in range(0, n):
        c = prefix(x, i) + suffix(x, i)
        b.append(c)
    fmax = b[0]
    r = 0
    for i in range(1, n):
        if fmax > b[i]:
           fmax = b[i]
           r = i
    print("Output: " + str(r+1))