import requests
from bs4 import BeautifulSoup
import csv
import json

url = "https://coinmarketcap.com/all/views/all/"

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/105.0.0.0 Mobile Safari/537.36 ",
    "accept": "application/json, text/plain, */*"
}

req = requests.get(url, headers=headers)

src = req.text

with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)