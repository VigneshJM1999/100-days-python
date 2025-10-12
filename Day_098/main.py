import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

SENDER_EMAIL = os.environ.get('EMAIL_USER')
SENDER_PASSWORD = os.environ.get('EMAIL_PASS')
RECEIVER_EMAIL = "boss_email@example.com"

try:
    with open('email_template.txt', 'r') as f:
        email_body_template = f.read()
except FileNotFoundError:
    print("Error: 'email_template.txt' not found. Please create it.")
    exit()

current_month = date.today().strftime("%B")
email_body = email_body_template.format(current_month=current_month)

message = MIMEMultipart("alternative")
message["Subject"] = "Checking In: Performance and Compensation"
message["From"] = SENDER_EMAIL
message["To"] = RECEIVER_EMAIL

message.attach(MIMEText(email_body, "plain"))

SMTP_SERVER = "smtp.gmail.com"
PORT = 465

context = ssl.create_default_context()

print("Connecting to email server...")
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        if SENDER_EMAIL and SENDER_PASSWORD:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("Login successful. Sending email...")
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
            print("Email successfully sent!")
        else:
            print("Error: EMAIL_USER and EMAIL_PASS environment variables not set.")
            print("Please follow the instructions in instructions.md")

except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Check your email/password or 'App Password'.")
except Exception as e:
    print(f"An error occurred: {e}")

