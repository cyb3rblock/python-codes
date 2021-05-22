from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.google.com")
s = BeautifulSoup(r.content,"html.parser")
print(s.prettify())