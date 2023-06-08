import requests
from bs4 import BeautifulSoup
import csv
import json

# url = "https://coinmarketcap.com/all/views/all/"
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/105.0.0.0 Mobile Safari/537.36 ",
#     "accept": "application/json, text/plain, */*"
# }
#
# req = requests.get(url, headers=headers)
#
# src = req.text
#
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open("index.html", "r", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

table_headers = soup.find(class_="cmc-table__table-wrapper-outer").find("thead").find("tr").find_all("th")

csv_headers = []

for item in table_headers:
    csv_headers.append(item.text)

with open("currency.csv", "w", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        (
            csv_headers
        )
    )

print(csv_headers)
