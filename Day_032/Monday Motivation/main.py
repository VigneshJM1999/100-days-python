import smtplib
import datetime as dt
import random

email = "example@email.com"
password = "example_password"

now = dt.datetime.now()

if now.weekday() == 4:
    with open("quotes.txt", "r") as file:
        q_list = file.readlines()
        quote = random.choice(q_list).strip()

    to_address = "test@email.com"
    subject = "Quote of the Day!"
    msg = f"To: {to_address}\nSubject: {subject}\n\n{quote}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_address,
            msg=msg
        )
