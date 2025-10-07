import smtplib
import os
from email.message import EmailMessage

def send(report_path, recipient):
    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")

    msg = EmailMessage()
    msg["Subject"] = "Website Audit Report"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content("Hi,\n\nPlease find the attached audit report for your website.\n\nRegards,\nDeepanshu")

    with open(report_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(report_path)
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print(f"📤 Email sent to {recipient}")
