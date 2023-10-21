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

# web driver setting
service = Service(ChromeDriverManager().install())
chromeOption = webdriver.ChromeOptions()
chromeOption.add_experimental_option('detach', True)
# chromeOption.add_argument('headless')
driver = webdriver.Chrome(service=service, options=chromeOption)


# crawling 벤 방지
seed = np.random.randint(100)
np.random.seed(seed)
time_sleep = np.random.randint(5)

# 요소 존재 확인
def check_exists(driver, class_name):
    try:
        driver.find_element(by=By.CLASS_NAME, value=class_name)
    except NoSuchElementException:
        return False
    return True

def crawling(i_url):
    urls = i_url
    print(i_url)
    rest_list = []
    for url in urls:
        print(url)
        driver.get(url)
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        name = ""
        address = ""
        tele = ""
        open_time = ""
        menus = []


        if check_exists(driver, 'Ozh8q'):
            print('if')
            menu_images = soup.select('a.Ozh8q > div.ZHqBk > div.place_thumb > div.lazyload-wrapper >img')
            print(menu_images[3]['src'])
        else:
            print('else')
            continue
    driver.quit()

crawling(['https://m.place.naver.com/restaurant/1351531666/home'])

