import os 
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()

EMAIL_ADDRESS = os.environ.get("EMAIL_SENDER")

EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

def send_email(receiver, subject, body):
  try:
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = receiver
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    return "Email sent successfully"
  except Exception as e:
    return "Error sending email: {}".format(str(e))