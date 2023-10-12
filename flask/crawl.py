from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import csv
import json
import numpy as np

# Fc1rA # 가게 이름
# LDgIH # 주소
# xlx7Q # 전화번호
# time # 영업시작 시간
# MENyI # 메뉴이름
# gl2cc # 메뉴 가격

# web driver setting
service = Service(ChromeDriverManager().install())
chromeOption = webdriver.ChromeOptions()
chromeOption.add_experimental_option('detach', True)
chromeOption.add_argument('headless')
driver = webdriver.Chrome(service=service, options=chromeOption)

# crawling 벤 방지
seed = np.random.randint(100)
np.random.seed(seed)
time_sleep = np.random.randint(5)

# 요소 존재 확인
def check_exists(class_name):
    try:
        driver.find_element(by=By.CLASS_NAME, value=class_name)
    except NoSuchElementException:
        return False
    return True

# f = open('맛집.csv', 'a',encoding='utf-8')
# csvWriter = csv.writer(f)
#
# csv_list = []


# Fc1rA # 가게 이름
# LDgIH # 주소
# xlx7Q # 전화번호
# time # 영업시작 시간
# MENyI # 메뉴이름
# gl2cc # 메뉴 가격

# ihmWt # 메뉴이름2
# awlpp # 메뉴가격2

def crawling(i_url):
    urls = i_url
    print(i_url)
    rest_list = []
    for url in urls:
        print(url)
        driver.get(url)
        time.sleep(0.3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        name = ""
        address = ""
        tele = ""
        open_time = ""
        menus = []

        if check_exists('Fc1rA'):
            time.sleep(time_sleep)
            name = soup.select('.Fc1rA')[0].text
        if check_exists('LDgIH'):
            time.sleep(time_sleep)
            address = soup.select('.LDgIH')[0].text
        if check_exists('xlx7Q'):
            time.sleep(time_sleep)
            tele = soup.select('.xlx7Q')[0].text
        # if check_exists('w9QyJ'):
        #     if check_exists('_UCia'):
        #         button = driver.find_elements(by=By.CLASS_NAME, value='w9QyJ')[0]
        #         button.click()
        #         html = driver.page_source
        #         soup = BeautifulSoup(html, 'html.parser')
        #
        #     open_time = soup.select('time')[0].text

        if check_exists('MENyI'):
            time.sleep(time_sleep)
            menu_names = soup.select('.MENyI')
        else:
            time.sleep(time_sleep)
            menu_names = soup.select('.ihmWt')
        if check_exists('gl2cc'):
            time.sleep(time_sleep)
            menu_price = soup.select('.gl2cc')
        else:
            time.sleep(time_sleep)
            menu_price = soup.select('.awlpp')

        menunames = []
        menuprice = []

        for i in range(len(menu_names)):
            menunames.append(menu_names[i].text)
            menuprice.append(menu_price[i].text)
            menus.append([menu_names[i].text, menu_price[i].text])

        rest = {
            "name": name,
            "address": address,
            "tel": tele
            # "openingHours": open_time
        }

        menu = dict(zip(menunames, menuprice))

        rest["menuDtoList"] = menu

        print(rest)
        rest_list.append(rest)
    # csvWriter.writerows(csv_list)
    # f.close()
    # linktxt.close()

    driver.quit()

    return rest_list

