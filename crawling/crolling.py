from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://map.naver.com/v5/?c=15,0,0,0,dh")


wait(driver, 25).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input.input_search"))).send_keys('검단 맛집' + Keys.ENTER)
# time.sleep(25)

# driver.find_element(By.CSS_SELECTOR, "#sidebar > navbar > perfect-scrollbar > div > div.ps-content > div > ul > li:nth-child(1) > a > span.navbar_text").click()

# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"input.input_search").send_keys("검단 맛집" + Keys.ENTER)

time.sleep(100)
