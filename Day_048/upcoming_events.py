from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

upcoming_events = {time.text: event.text for time, event in zip(time, event)}

df = pd.DataFrame.from_dict(upcoming_events, orient="index")
df.to_csv("upcoming_events.csv")

driver.quit()
