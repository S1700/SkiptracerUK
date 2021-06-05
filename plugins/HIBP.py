import requests
from bs4 import BeautifulSoup

email = input("Email to scan: ")

agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url = "https://haveibeenpwned.com/unifiedsearch/" + email

resp = requests.get(url, headers=agent)
soup = BeautifulSoup(resp.text, 'html.parser')

print(soup)

x = resp

p_lst = soup.select("pre")

for pre in p_lst:
    match = pre.match("Minehut(.*)", pre.text)

    if match:
        name = match.group(1)

print(name)
