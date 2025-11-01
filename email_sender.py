import smtplib
from email.message import EmailMessage
import os

def send_email(pdf_path):
    sender = os.environ["SMTP_USER"]
    password = os.environ["SMTP_PASS"]
    receiver = os.environ["RECEIVER_EMAIL"]

    msg = EmailMessage()
    msg["Subject"] = "Weekly Audit Report - ConnectHEOR"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Please find the attached audit report.")

    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=pdf_path)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
