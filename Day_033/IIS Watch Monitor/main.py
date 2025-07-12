import requests
from datetime import datetime, timezone
import time
import smtplib

EMAIL = "test_sender@gmail.com"
PASSWORD = "test_password"

MY_LATITUDE = 13.082680
MY_LONGITUDE = 80.270721

parameters = {
    "lat":MY_LATITUDE,
    "lng":MY_LONGITUDE,
    "formatted":0,
}

def iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    return ((MY_LATITUDE - 5) <= iss_latitude <= (MY_LATITUDE + 5)) and ((MY_LONGITUDE - 5) <= iss_longitude <= (MY_LONGITUDE + 5))

def is_dark():
    now = datetime.now(timezone.utc)
    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    return now.hour < sunrise or now.hour > sunset

def send_mail():
    to_address = "test_receiver@gmail.com"
    subject = "Watch ISS"
    message = f"Subject: {subject}\nTo: {to_address}\n\nHi,\n\nThe ISS is nearby.\n\nGo and watch it now!\n\nThanks."
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=to_address,
            msg=message
        )

while True:
    sleep_seconds = 60
    if iss_overhead() and is_dark():
        send_mail()
        sleep_seconds = 600
    time.sleep(sleep_seconds)
