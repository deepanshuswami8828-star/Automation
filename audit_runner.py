from pdf_generator import create_pdf
from email_sender import send_email

def run_audit():
    audit_data = {
        "site": "connectheor.com",
        "status": "Live",
        "performance": "Good",
        "seo": "Checked"
    }
    pdf_path = create_pdf(audit_data)
    send_email(pdf_path)

if __name__ == "__main__":
    run_audit()
