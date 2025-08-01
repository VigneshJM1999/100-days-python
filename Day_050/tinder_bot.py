import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("FB_EMAIL")
PASSWORD = os.getenv("FB_PASSWORD")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com")

time.sleep(5)
try:
    login_btn = driver.find_element(By.LINK_TEXT, "Log in")
    login_btn.click()
except:
    driver.find_element(By.XPATH, '//button[contains(text(),"Log in")]').click()

time.sleep(3)
fb_login = driver.find_element(By.XPATH, '//button/span[contains(text(),"Log in with Facebook")]')
fb_login.click()

time.sleep(5)
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)

driver.find_element(By.ID, "email").send_keys(EMAIL)
driver.find_element(By.ID, "pass").send_keys(PASSWORD)
driver.find_element(By.ID, "pass").send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
time.sleep(10)

try:
    driver.find_element(By.XPATH, '//button[contains(text(), "Allow")]').click()
except:
    pass

time.sleep(2)
try:
    driver.find_element(By.XPATH, '//button[contains(text(), "Enable")]').click()
except:
    pass

for _ in range(50):
    time.sleep(2)
    try:
        like_btn = driver.find_element(By.XPATH, '//button[@aria-label="Like"]')
        like_btn.click()
    except (NoSuchElementException, ElementClickInterceptedException):
        try:
            driver.find_element(By.XPATH, '//button[contains(text(), "Not interested")]').click()
        except:
            pass

driver.quit()
