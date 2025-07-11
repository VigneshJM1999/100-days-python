import smtplib
import datetime as dt
import random
import pandas

email = "example@email.com"
password = "example_password"

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {
    (row["month"], row["day"]): row for index, row in data.iterrows()
}

today = dt.date.today()

today_tuple = (today.month, today.day)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    random_number = random.randint(1, 3)
    chosen_file = f"letter_templates/letter_{random_number}.txt"

    with open(chosen_file, "r") as file:
        template = file.read()

    wishes = template.replace("[NAME]", birthday_person["name"]).strip()
    to_address = birthday_person["email"].strip()
    subject = "Happy Birthday!"
    msg = f"Subject: {subject}\nTo: {to_address}\n\n{wishes}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_address,
            msg=msg
        )
