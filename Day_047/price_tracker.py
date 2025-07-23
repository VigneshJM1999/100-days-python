import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

TARGET = 100
URL= "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=URL, headers=header)
shop_website = response.text
soup =  BeautifulSoup(shop_website, "html.parser")
price_tag = soup.find("span", class_="aok-offscreen")
price = float(price_tag.get_text().split()[0].replace("$", ""))
name_tag = soup.select("h1 span")[0]
name = " ".join(name_tag.get_text().split())

if price <= TARGET:
    alert = f"{name} is now ${price}.\n{URL}"
    to_address = os.environ["TO_EMAIL"]
    subject = "Amazon Price Alert!"

    message = MIMEMultipart()
    message["From"] = email
    message["To"] = to_address
    message["Subject"] = subject

    message.attach(MIMEText(alert, "plain", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_address,
            msg=message.as_string()
        )
