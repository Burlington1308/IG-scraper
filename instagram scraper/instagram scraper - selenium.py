from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

import os
import wget

driver = webdriver.Chrome('C:/Users/Adminbk/Desktop/chrome_driver/chromedriver.exe')
driver.get("https://www.instagram.com/")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))) 

username.clear()
password.clear()

username.send_keys("blackmotif90")
password.send_keys("fortunate")

log_in = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(3)
not_now = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
time.sleep(3)
not_now2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

searchbox = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = 'msthunjwas'
searchbox.send_keys(keyword)
time.sleep(2)
searchbox.send_keys(Keys.ENTER)
searchbox.send_keys(Keys.RETURN)

driver.execute_script("window.scrollTo(0, 4000);")

time.sleep(3)
images = driver.find_elements(by=By.TAG_NAME , value='img')
time.sleep(3)
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, keyword)

os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
