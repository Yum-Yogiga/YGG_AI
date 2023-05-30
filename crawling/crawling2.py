from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import csv
import requests

search = input('검색어를 입력하세요: ')


# web driver setting
service = Service(ChromeDriverManager().install())
chromeOption = webdriver.ChromeOptions()
chromeOption.add_experimental_option('detach', True)
chromeOption.add_argument('headless')
driver = webdriver.Chrome(service = service, options = chromeOption)


# naver map searching url
url = f'https://m.map.naver.com/search2/search.naver?query={quote_plus(search)}&sm=hty&style=v5'

driver.get(url)

time.sleep(3)

item_list = []
temp_list = driver.find_elements(By.CSS_SELECTOR, '.a_item.a_item_distance._linkSiteview')
for i in temp_list:
    item_list.append(i.get_attribute('data-cid')) # store number

# csv file
f = open(f'{search}.csv', 'w')
csvWriter = csv.writer(f)
csv_list =[['가게 이름',1,2,3,4,5]]

f2 = open('test.html','w',encoding='UTF-8')

# link traversal review data save
for it in item_list[0:1]:
    url = f'https://m.place.naver.com/restaurant/{it}/review/visitor'
    html1 = requests.get(url)
    html1.encoding = 'UTF-8'
    f2.write(html1.text)

    # driver.get(url)
    # time.sleep(0.3)
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # review_list = soup.select('.nWiXa')
    # title = soup.select_one('#_header').text
    # temp = []
    # temp.append(title)

    # for i in review_list:
    #     temp.append(i.text)
    #
    # csv_list.append(temp)

# csvWriter.writerows(csv_list)
f.close()
f2.close()

driver.quit()

# button class Tvx37