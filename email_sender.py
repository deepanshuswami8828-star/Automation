import smtplib
from email.message import EmailMessage
import os

def send_email(pdf_path):
    sender = os.environ.get("SMTP_USER")
    password = os.environ.get("SMTP_PASS")
    receiver = os.environ.get("RECEIVER_EMAIL")

    print("📤 Preparing to send email...")
    print(f"Sender: {sender}")
    print(f"Receiver: {receiver}")
    print(f"PDF Path: {pdf_path}")

    # Create the email message
    msg = EmailMessage()
    msg["Subject"] = "Weekly Audit Report - ConnectHEOR"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Please find the attached audit report.")

    try:
        # Attach the PDF
        with open(pdf_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename=os.path.basename(pdf_path)
            )
        print("📎 PDF attached successfully.")

        # Send the email via Gmail SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            print("🔐 SMTP login successful.")
            smtp.send_message(msg)
            print("✅ Email sent successfully to", receiver)

    except Exception as e:
        print("❌ Email sending failed:", str(e))
