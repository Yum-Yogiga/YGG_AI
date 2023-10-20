from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
import csv
import json
import numpy as np
import urllib.request

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

# chromeOption.add_argument('headless')
#chromeOption.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')
# chromeOption.add_argument('headless')

# crawling 벤 방지
seed = np.random.randint(100)
np.random.seed(seed)
time_sleep = np.random.randint(3)

# 요소 존재 확인
def check_exists(driver, class_name):
    try:
        driver.find_element(by=By.CLASS_NAME, value=class_name)
    except NoSuchElementException:
        return False
    return True

# f = open('맛집.csv', 'a',encoding='utf-8')
# csvWriter = csv.writer(f)
#
# csv_list = []

# place_thumb::before # 메뉴 사진
# Fc1rA # 가게 이름
# LDgIH # 주소
# xlx7Q # 전화번호
# time # 영업시작 시간
# MENyI # 메뉴이름
# gl2cc # 메뉴 가격

# ihmWt # 메뉴이름2
# awlpp # 메뉴가격2

def crawling(i_url):
    driver = webdriver.Chrome(service=service, options=chromeOption)
    print('in')
    urls = i_url
    print(i_url)
    rest_list = []

    for url in urls:
        print(url)
        driver.get(url)
        time.sleep(time_sleep)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        name = ""
        address = ""
        tele = ""
        open_time = ""
        menus = []

        if check_exists(driver,'Fc1rA'):
            # time.sleep(time_sleep)
            name = soup.select('.Fc1rA')[0].text
        if check_exists(driver, 'LDgIH'):
            # time.sleep(time_sleep)
            address = soup.select('.LDgIH')[0].text
        if check_exists(driver, 'xlx7Q'):
            # time.sleep(time_sleep)
            tele = soup.select('.xlx7Q')[0].text
        # if check_exists('w9QyJ'):
        #     if check_exists('_UCia'):
        #         button = driver.find_elements(by=By.CLASS_NAME, value='w9QyJ')[0]
        #         button.click()
        #         html = driver.page_source
        #         soup = BeautifulSoup(html, 'html.parser')
        #
        #     open_time = soup.select('time')[0].text

        if check_exists(driver,'MENyI'):
            # time.sleep(time_sleep)
            menu_names = soup.select('.MENyI')
        else:
            # time.sleep(time_sleep)
            menu_names = soup.select('.ihmWt')
        if check_exists(driver, 'gl2cc'):
            # time.sleep(time_sleep)
            menu_price = soup.select('.gl2cc')
        else:
            # time.sleep(time_sleep)
            menu_price = soup.select('.awlpp')
        menu_images = []
        menunames = []
        menuprice = []
        menuimg = []

        # 메뉴 이미지가 있는 경우
        if check_exists(driver, 'ZHqBk'):
            # 메인에 비디오가 있는 경우
            # if check_exists(driver, 'pzp-ui-dimmed'):
            print("video")
            menu_images = soup.select('a.Ozh8q > div.ZHqBk > div.place_thumb >img')
            print(menu_images)
            for i in range(len(menu_names)):
                menunames.append(menu_names[i].text)
                menuprice.append(menu_price[i].text)
                menuimg.append(menu_images[i]['src'])
                menus.append([menu_names[i].text, menu_price[i].text])

            # else:
            #     print("no video")
            #     # menu_images = soup.select('a.Ozh8q > div.ZHqBk > div.place_thumb > div.lazyload-wrapper > img')
            #     menu_images = soup.select('a.Ozh8q > div.ZHqBk > div.place_thumb > img')
            #     print(menu_images)
            #     for i in range(len(menu_names)):
            #         menunames.append(menu_names[i].text)
            #         menuprice.append(menu_price[i].text)
            #         menuimg.append(menu_images[i]['src'])
            #         menus.append([menu_names[i].text, menu_price[i].text])
        else:
            print("else")
            for i in range(len(menu_names)):
                menunames.append(menu_names[i].text)
                menuprice.append(menu_price[i].text)
                menuimg.append("none")
                menus.append([menu_names[i].text, menu_price[i].text])



        rest = {
            "name": name,
            "address": address,
            "tel": tele
            # "openingHours": open_time
        }

        menu = dict(zip(menunames,zip(menuprice,menuimg)))

        rest["menuDtoList"] = menu

        print(rest)
        rest_list.append(rest)
    # csvWriter.writerows(csv_list)
    # f.close()
    # linktxt.close()

    driver.quit()

    return rest_list

# video 있는 거
# crawling(['https://m.place.naver.com/restaurant/1721729164/home','https://m.place.naver.com/restaurant/1759441377/home','https://m.place.naver.com/restaurant/1721729164/home'])

# 비디오 없는거
# crawling(['https://m.place.naver.com/restaurant/1759441377/home'])