import urllib.request as url_req
from bs4 import BeautifulSoup

target_href = "http://www.succulents.jp/country_list.html"

html = url_req.urlopen(target_href)
soup = BeautifulSoup(html,"lxml")
for tag in soup.select("td.cnt_ne"):
    print(tag.string)

