from create_pdf.create_pdf import create_pdf
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
        "deadlinks": 10,
        "roastd": {"score": "82%", "issues": 5},
        "seomator": {"seo_score": "78%", "mobile": "Good"},
        "sitechecker": {"health": "74%", "broken_links": 3},
        "pagespeed": {"mobile": "65", "desktop": "88"},
        "upguard": {"ssl": "Valid", "malware": "None", "leaks": "No"}
    }

    pdf_path = create_pdf(audit_data)
    send_email(pdf_path)

if __name__ == "__main__":
    run_audit()
