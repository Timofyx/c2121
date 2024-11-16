from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "sc-b3fc6b7-0"})
    res = soup_list[1].find("span")
    print(str(res)[6:-7])

    for i in soup_list:
        print(i)