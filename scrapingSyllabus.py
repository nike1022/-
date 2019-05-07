
import requests
from bs4 import BeautifulSoup

html = requests.get('https://news.yahoo.co.jp')
yahoo = BeautifulSoup(html.content, "html.parser")

for elem in yahoo.select("li.topicsListItem"):
    print(elem.getText())               # <a href="">テキスト</a>
    print(elem.find("a").get("href"))   # <a href="URL">
