from metrics.fetch_metrics import fetch_psi_metrics
from pdf.generate_pdf import generate_pdf
from email.send_email import send_email
import os

# Load URLs from file
urls = open("urls.txt").read().splitlines()

# Load secrets from environment variables
api_key = os.getenv("PSI_API_KEY")
sender = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")

# Collect metrics for each URL
report = {}
for url in urls:
    report[url] = fetch_psi_metrics(url, api_key)

# Generate PDF report
generate_pdf(report)

# Send report via email
send_email(
    recipient="client@example.com",
    subject="Website Audit Report",
    body="Attached is your latest website audit.",
    attachment_path="audit_report.pdf",
    sender=sender,
    password=password
)
