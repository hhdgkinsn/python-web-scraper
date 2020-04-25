from bs4 import BeautifulSoup
import requests
import json

news = requests.get("https://www.bbc.co.uk/news").text
soup = BeautifulSoup(news, 'lxml')


site_container = soup.find("div", id="news-top-stories-container")
unique_headlines = set(site_container.find_all(class_="gs-c-promo-heading__title"))
uh_list = []
for headline in unique_headlines:
    uh_list.append(headline.text)

with open("news.json", "w") as data:
    json.dump(uh_list, data)



