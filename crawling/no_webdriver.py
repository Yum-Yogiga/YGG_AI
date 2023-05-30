from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import requests
import time

search = input('검색어를 입력하세요: ')
url = f'http://m.map.naver.com/search2/search.naver?query={quote_plus(search)}&sm=hty&style=v5'
print(url)

f = open('file.html','w')

response = requests.get(url)
print(response)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
f.write(html)
f.close()

item_list = []
temp_list = soup.select('#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview')
print(temp_list)
