from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
job = "python developer"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
sleep(10)

email_tag = driver.find_element(By.CSS_SELECTOR, "#username")
password_tag = driver.find_element(By.CSS_SELECTOR, "#password")
sign_in_btn = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container")

email_tag.send_keys(email)
password_tag.send_keys(password)
sign_in_btn.click()

search_tag = driver.find_element(By.CSS_SELECTOR, "#global-nav-search input.search-global-typeahead__input")
search_tag.send_keys(job)
search_tag.send_keys(Keys.ENTER)

sleep(15)
job_tag = driver.find_element(By.CSS_SELECTOR, "#search-reusables__filters-bar > ul > li:nth-child(1) > button")
job_tag.click()

sleep(15)

job_container_tags = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")
count = 0

for job in job_container_tags:
        job.click()
        job_save_btn = driver.find_element(By.CSS_SELECTOR, "span.jobs-save-button__text")
        job_save_btn.click()
        follow_btn = driver.find_element(By.CSS_SELECTOR, "div.jobs-company__box button span")
        follow_btn.click()
        sleep(5)