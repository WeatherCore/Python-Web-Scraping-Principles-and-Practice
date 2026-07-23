import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://quotes.toscrape.com"
url = "/page/1/"
all_quotes = []

# 模拟浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

while url:
    full_url = base_url + url
    try:
        # 设置超时时间，防止程序卡死
        res = requests.get(full_url, headers=headers, timeout=10)
        if res.status_code != 200:
            print(f"页面访问失败 {full_url} 状态码：{res.status_code}")
            break

        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            span_tag = q.find("span", class_="text")
            small_tag = q.find("small", class_="author")
            # 防御判断，避免标签缺失导致程序崩溃
            if span_tag and small_tag:
                text = span_tag.get_text(strip=True)
                author = small_tag.get_text(strip=True)
                all_quotes.append([text, author])

        # 获取下一页链接
        next_li = soup.find("li", class_="next")
        url = next_li.a["href"] if next_li else None

        # 礼貌延时，降低服务器压力
        time.sleep(0.5)

    except Exception as err:
        print("请求发生异常：", err)
        break

# utf-8-sig 解决Windows Excel打开CSV中文乱码问题
with open("quotes2.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(all_quotes)

print(f"抓取完成，总计 {len(all_quotes)} 条名言数据")