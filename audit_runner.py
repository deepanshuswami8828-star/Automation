from pdf_generator import create_pdf
from email_sender import send_email
from datetime import datetime

def run_audit():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🕒 Starting audit at {timestamp}")

    audit_data = {
        "site": "connectheor.com",
        "status": "Live",
        "performance": "Good",
        "seo": "Checked",
        "timestamp": timestamp
    }

    print("📄 Generating PDF report...")
    pdf_path = create_pdf(audit_data)
    print(f"✅ PDF generated: {pdf_path}")

    print("📬 Sending email with report...")
    send_email(pdf_path)
    print("✅ Email sent successfully.")

if __name__ == "__main__":
    run_audit()
