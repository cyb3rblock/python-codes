a = int(input("enter number to check\n"))
c = str(a*a)
g = len(c)
if g % 2 == 0:
    b = int(c[0:g//2])
    d = int(c[g//2:g])
    if b != 0 and d != 0 and b+d == a:
        print("kaprekar number")
    else:
        print("not kaprekar number")
else:
    b = int(c[0:(g+1)//2])
    d = int(c[(g+1)//2:g])
    e = int(c[0:(g-1)//2])
    f = int(c[(g-1)//2:g])
    if (b != 0 and d != 0 and b + d == a) or (e != 0 and f != 0 and e + f == a):
        print("kaprekar number")
    else:
        print("not kaprekar number")
