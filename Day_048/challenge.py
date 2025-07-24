from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("F_NAME")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("L_NAME")

e_mail = driver.find_element(By.NAME, value="email")
e_mail.send_keys("TEST@GMAIL.COM")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()

