from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import csv


location_list = ['홍대','연남','상수','합정']
restaurant_list = ['한식','일식','중식','양식','분식','고깃집']

# 검색어 리스트
search_list = []

# for ll in location_list:
#     for rl in restaurant_list:
#         search_string = ll + " " + rl
#         search_list.append(search_string)

sl_file = open('link.txt','r')
while True:
    temp = sl_file.readline()
    if not temp: break
    search_list.append(temp)


# web driver setting
service = Service(ChromeDriverManager().install())
chromeOption = webdriver.ChromeOptions()
chromeOption.add_experimental_option('detach', True)
chromeOption.add_argument('headless')
driver = webdriver.Chrome(service = service, options = chromeOption)


item_list = []
# linktxt = open('link.txt','w')

count = 0
# # naver map searching url
# for sl in search_list:
#     # url = f'https://m.map.naver.com/search2/search.naver?query={quote_plus(sl)}&sm=hty&style=v5'
#     url = sl
#     driver.get(url)
#
#     time.sleep(3)
#
#     temp_list = driver.find_elements(By.CSS_SELECTOR, '.a_item.a_item_distance._linkSiteview')
#     for i in temp_list:
#         storeNumber = i.get_attribute('data-cid')
#         item_list.append(storeNumber) # store number
#         # linktxt.write(f'https://m.place.naver.com/restaurant/{storeNumber}/review/visitor' + '\n')
#         # count += 1
# # linktxt.close()

# csv file
f = open('맛집.csv', 'a')
csvWriter = csv.writer(f)
# csv_list =[['가게 이름',1,'인원 수',2,'인원 수',3,'인원 수',4,'인원 수',5,'인원 수',6,'인원 수',7,'인원 수',8,'인원 수',9,'인원 수',10,'인원 수','링크']]
csv_list = []
# link traversal review data save
for it in search_list[20:]:
    # url = f'https://m.place.naver.com/restaurant/{it}/review/visitor'
    url = it
    print(count)
    count = count + 1

    driver.get(url)
    time.sleep(0.3)
    button = driver.find_elements(by=By.CLASS_NAME,value='Tvx37')[-1]
    button.click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    review_list = soup.select('.nWiXa')
    keywordPerson_list = soup.select('.TwM9q')
    title = soup.select_one('#_header').text
    temp = [title]

    # print(keywordPerson_list[0].text)
    # for i,j in review_list, keywordPerson_list:
    #     print(j.text)
    #     temp.append(i.text)
    for i in range(10):
        temp.append(review_list[i].text.strip("\""))
        temp.append(keywordPerson_list[i].text.strip('이 키워드를 선택한 인원'))
    temp.append(f'https://map.naver.com/v5/entry/place/{it}?c=15,0,0,0,dh')
    csv_list.append(temp)
    if count % 10 == 0:
        csvWriter.writerows(csv_list)
        csv_list = []

csvWriter.writerows(csv_list)
f.close()
# linktxt.close()

driver.quit()
# button class Tvx37
# 인원수 class TwM9q
# new xpath =
# /html/body/div[3]/div/div/div/div[7]/div[2]/div[1]/div/div/div[2]/ul/li[2]/div[2]/span[2]
# old xpath =
# /html/body/div[3]/div/div/div/div[7]/div[2]/div[1]/div/div/div[2]/a
# new xpath
# //*[@id="app-root"]/div/div/div/div[7]/div[2]/div[1]/div/div/div[2]/ul/li[2]/div[2]/span[2]
# old xpath
#//*[@id="app-root"]/div/div/div/div[7]/div[2]/div[1]/div/div/div[2]/a
