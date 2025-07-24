from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
no_of_article = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')

# print(no_of_article.text)

content_portal = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portal.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# driver.quit()
