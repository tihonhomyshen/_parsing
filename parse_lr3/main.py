# -*- coding: cp1251 -*-
import requests
from bs4 import BeautifulSoup
import json
import csv

# url = "https://health-diet.ru/table_calorie"


#
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
}
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)
#
# with open("index.html", encoding="utf-8") as file:
#     src = file.read()
#
# Сохраняем главную страницу локально

# soup = BeautifulSoup(src, "lxml")
#
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
# for item in all_products_hrefs:
#     print(item)
#
#
# all_categories = {}
#
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item["href"]
#     print(f"{item_text} : {item_href}")
#
#     all_categories[item_text] = item_href
#
# print(all_categories)

# Пробегаемся по классу с названием категории, записываем название: ссылка в словарь

# with open("all_categories.json", "w", encoding="utf-8") as file:
#    json.dump("all_categories.json", file, indent=4, ensure_ascii=False)

with open("all_categories.json") as file:
    all_categories = json.load(file)

print(all_categories)
iteration_count = int(len(all_categories)) - 1
count = 0
print(f"Всего итераций: {iteration_count}")
for category_name, category_href in all_categories.items():
    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open (f"data/{count}_{category_name}.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open (f"data/{count}_{category_name}.html", encoding="utf-8") as file:
        file.read()

    soup = BeautifulSoup(src, "lxml")

    alert_block = soup.find (class_="uk-alert-danger")
    if alert_block is not None:
        continue

    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    table_head1 = soup.select(".mzr-tc-group-table tr th")
    print(table_head, table_head1, sep="\n")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f"data/{count}_{category_name}.csv", "w", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    # собираем данные продуктов
    products_data = soup.select('.mzr-tc-group-table tbody tr')

    product_info = []
    for item in products_data:
        products_tds = item.find_all("td")

        title = products_tds[0].find("a").text
        calories = products_tds[1].text
        proteins = products_tds[2].text
        fats = products_tds[3].text
        carbohydrates = products_tds[4].text

        product_info.append(
            {
                "title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )

        with open(f"data/{count}_{category_name}.csv", "a", encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates
                )
            )
        with open(f"data/{count}_{category_name}.json", "w", encoding="utf-8-sig") as file:
            json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
