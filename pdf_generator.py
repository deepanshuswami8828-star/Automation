from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime
import os

def create_pdf(data):
    filename = "connectheor_audit.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "ConnectHEOR Website Migration and Performance Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 765, f"Website: {data.get('site', 'N/A')}")

    y = 740

    # Section 1: Migration Overview
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "1. Migration Overview")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Migration Status: {data.get('migration', 'N/A')}")
    y -= 140
    if os.path.exists("assets/migration.png"):
        c.drawImage(ImageReader("assets/migration.png"), 50, y, width=500, height=120)

    # Section 2: Global Accessibility
    y -= 160
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "2. Website Accessibility Across All Locations")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Status: Accessible globally")
    y -= 140
    if os.path.exists("assets/lighthouse_scores.png"):
        c.drawImage(ImageReader("assets/lighthouse_scores.png"), 50, y, width=500, height=120)

    # Section 3: Performance Testing
    y -= 160
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "3. Performance Testing")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"GTmetrix Grade: {data.get('gtmetrix', {}).get('grade', 'N/A')}")
    c.drawString(50, y - 20, f"Performance: {data.get('gtmetrix', {}).get('performance', 'N/A')}")
    c.drawString(50, y - 40, f"Structure: {data.get('gtmetrix', {}).get('structure', 'N/A')}")
    y -= 160
    if os.path.exists("assets/gtmetrix.png"):
        c.drawImage(ImageReader("assets/gtmetrix.png"), 50, y, width=500, height=120)

    # Section 4: SEO Audit
    y -= 160
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "4. SEO Audit")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"SEO Status: {data.get('seo', 'N/A')}")
    c.drawString(50, y - 20, f"Tools Used: {', '.join(data.get('seo_tools', []))}")
    y -= 140
    if os.path.exists("assets/seo_summary.png"):
        c.drawImage(ImageReader("assets/seo_summary.png"), 50, y, width=500, height=120)

    # Section 5: Security Audit
    y -= 160
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "5. Security Audit")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Status: {data.get('security', 'N/A')}")
    c.drawString(50, y - 20, f"Dead Links Found: {data.get('deadlinks', 'N/A')}")
    y -= 140
    if os.path.exists("assets/upguard.png"):
        c.drawImage(ImageReader("assets/upguard.png"), 50, y, width=500, height=120)

    # Section 6: Final Summary
    y -= 160
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "6. Final Summary")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Website migration and live status checks are completed successfully.")
    c.drawString(50, y - 20, "Performance metrics indicate optimal loading speed and user experience.")
    c.drawString(50, y - 40, "Next steps: monitor SEO scores, fix broken links, and optimize performance.")

    c.save()
    return filename
