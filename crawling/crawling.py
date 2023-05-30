from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import csv

search = input('검색어를 입력하세요: ')

# web driver setting
service = Service(ChromeDriverManager().install())
chromeOption = webdriver.ChromeOptions()
chromeOption.add_experimental_option('detach', True)
# chromeOption.add_argument('headless')
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
csv_list =[['가게 이름',1,2,3,4,5,6,7,8,9,10,'링크']]

# link traversal review data save
for it in item_list[0:3]:
    url = f'https://m.place.naver.com/restaurant/{it}/review/visitor'
    driver.get(url)
    time.sleep(0.3)
    button = driver.find_element(by=By.XPATH,value='//*[@id="app-root"]/div/div/div/div[7]/div[2]/div[1]/div/div/div[2]/a')
    button.click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    review_list = soup.select('.nWiXa')
    title = soup.select_one('#_header').text
    temp = [title]

    for i in review_list:
        temp.append(i.text)
    temp.append(f'https://map.naver.com/v5/entry/place/{it}?c=15,0,0,0,dh')
    csv_list.append(temp)

csvWriter.writerows(csv_list)
f.close()

driver.quit()
# button class Tvx37