import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com"
url = "/page/1/"
all_quotes = []

while url:
    res = requests.get(base_url + url)
    soup = BeautifulSoup(res.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        all_quotes.append([text, author])

    next_page = soup.find("li", class_="next")
    url = next_page.a["href"] if next_page else None

# 保存CSV
with open("quotes1.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(all_quotes)

print("共爬取名言数：", len(all_quotes))