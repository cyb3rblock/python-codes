t = int(input(""))
while t > 0:
    t = t - 1
    n = input("")
    x = []
    for i in range(0,len(n)):
        if n[i] == '{' or n[i] == '[' or n[i] == '(':
            x.append(n[i])
        elif (n[i] == '}' and x[len(x)-1] == '{') or (n[i] == ']' and x[len(x)-1] == '[') or (n[i] == ')' and x[len(x)-1] == '('):
            x.pop()
        elif (n[i] == '}' and x[len(x)-1] != '{') or (n[i] == ']' and x[len(x)-1] != '[') or (n[i] == ')' and x[len(x)-1] != '('):
            print("NO")
            break
        if not x:
            print("YES")