import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=url)
website = response.text
soup = BeautifulSoup(website, "html.parser")
link_tag = soup.find_all("a", class_="property-card-link")
links = [link.get("href") for link in link_tag]

price_tag = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.get_text().split("+")[0] for price in price_tag]

address_tag = soup.find_all("address")
address_list = [address.get_text().replace('\n', '').replace('|', '').strip() for address in address_tag]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeyNUCy1JPTDo3kOQuCl3cKuFmQNs6RO05Xz0NgI61q3zwUhA/viewform")
sleep(2)

for i in range(len(links)):
    inputs_tag = driver.find_elements(By.CSS_SELECTOR, ".whsOnd")
    submit_tag = driver.find_element(By.CSS_SELECTOR, ".NPEfkd")

    form_link_address = inputs_tag[0]
    form_link_price = inputs_tag[1]
    form_link_links = inputs_tag[2]

    form_link_address.send_keys(address_list[i])
    form_link_price.send_keys(price_list[i])
    form_link_links.send_keys(links[i])

    submit_tag.click()
    sleep(2)

    submit_another_response = driver.find_element(By.CSS_SELECTOR, "a")
    submit_another_response.click()
    sleep(2)

driver.quit()
