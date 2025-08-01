import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

SIMILAR_ACCOUNT = "chefsteps"
INSTAGRAM_USERNAME = os.environ["INSTAGRAM_USERNAME"]
INSTAGRAM_PASSWORD = os.environ["INSTAGRAM_PASSWORD"]

class InstaFollower:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.login()

    def login(self):
        username_tag = self.driver.find_element(By.NAME, "username")
        username_tag.send_keys(INSTAGRAM_USERNAME)
        password_tag = self.driver.find_element(By.NAME, "password")
        password_tag.send_keys(INSTAGRAM_PASSWORD)
        password_tag.send_keys(Keys.ENTER)
        sleep(5)
        not_now = self.driver.find_element(By.XPATH, "//div[text()='Not now']")
        not_now.click()
        sleep(1)
        self.find_followers()

    def follow(self):
        sleep(5)
        wait = WebDriverWait(self.driver, 10)
        modal = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//div[contains(@class, "_aano")]')))
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        sleep(2)

        follow_buttons = self.driver.find_elements(By.XPATH, '//button[normalize-space()="Follow"]')
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, '//button[text()="Cancel"]')
                cancel.click()

    def find_followers(self):
        profile_url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.driver.get(profile_url)
        sleep(6)

        followers_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]")
        followers_link.click()
        sleep(3)
        self.follow()

insta = InstaFollower()
