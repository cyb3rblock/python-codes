import requests
f = open("hosts.txt", "r")
l = f.readlines()
f.close()
f = open("newhosts.txt", "a")
for i in l:
    a = i.split(sep=",")
    try:
        r = requests.get("http://"+a[0],timeout=10)
    except requests.RequestException as e:
        pass
    except requests.exceptions.Timeout as e2:
        pass
    else:
        if r.status_code == 200:
            print(a)
            f.write(a[0])
f.close()

