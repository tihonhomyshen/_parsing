from bs4 import BeautifulSoup
with open("materials/index.html", encoding="UTF-8") as file:
    src = file.read()

 # print(src)
soup = BeautifulSoup(src, "lxml")
title = soup.title
#print(title)
#print(title.text)
#print(title.string)
page_h1 = soup.find_all("h1")
print(page_h1)

for item in page_h1:
    print(item.text)

user_name = soup.find("div", class_="user__name").find("span").text
print(user_name)

user_name = soup.find("div", {"class": "user__name"}).find("span").text
print(user_name)

span_all = soup.find(class_="user__info").find_all("span")
print(span_all)

for item in span_all:
    print(item.text)

social_links = soup.find(class_="social__networks").find("ul").find_all("a")
print(social_links)

all_a = soup.find_all("a")
print(all_a)

for item in all_a:
    item_text = item.text
    item_url = item.get("href")
    print(f"{item_text}: {item_url}")

post_div = soup.find(class_="post__text").find_parent("div","user__post")
print(post_div)