from pdf_generator import create_pdf
from email_sender import send_email

def run_audit():
    audit_data = {
        "site": "connectheor.com",
        "status": "Live",
        "performance": "Good",
        "seo": "Checked",
        "migration": "Completed from SiteGround to Hostinger",
        "gtmetrix": {"grade": "D", "performance": "61%", "structure": "81%"},
        "seo_tools": ["SiteGuru", "Labrika", "Sitechecker"],
        "security": "No malware found",
        "deadlinks": 10
    }

    print("🕒 Starting audit...")
    pdf_path = create_pdf(audit_data)
    print(f"📄 PDF generated: {pdf_path}")
    send_email(pdf_path)

if __name__ == "__main__":
    run_audit()
