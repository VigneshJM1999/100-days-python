import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

PROMISED_UP = 100
PROMISED_DOWN = 100
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]

class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

        self.down_speed = 0
        self.up_speed = 0

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".start-button").click()
        time.sleep(45)
        self.down_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get("https://x.com/home")
        sleep(5)
        email_tag = self.driver.find_element(By.NAME, "text")
        email_tag.send_keys(TWITTER_EMAIL)
        sleep(2)
        email_tag.send_keys(Keys.ENTER)
        try:
            password_tag = self.driver.find_element(By.NAME, "password")
            password_tag.send_keys(TWITTER_PASSWORD)
            sleep(2)
            password_tag.send_keys(Keys.ENTER)
        except NoSuchElementException:
            sleep(2)
            username_tag = self.driver.find_element(By.NAME, "text")
            username_tag.send_keys(TWITTER_USERNAME)
            sleep(2)
            username_tag.send_keys(Keys.ENTER)
            sleep(2)

        password_tag = self.driver.find_element(By.NAME, "password")
        password_tag.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password_tag.send_keys(Keys.ENTER)
        sleep(4)
        post_compose = self.driver.find_element(By.XPATH, '//div[@role="textbox"]')
        post = f"Hey @reliancejio,\n\nWhy is my internet speed {self.down_speed}down/{self.up_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        post_compose.send_keys(post)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()

speed_tester = InternetSpeedTwitterBot()
speed_tester.get_internet_speed()
