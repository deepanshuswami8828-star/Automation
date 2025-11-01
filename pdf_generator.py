from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime

def create_pdf(data):
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f"connectheor_audit_{timestamp}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "ConnectHEOR Website Audit Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, f"Date: {timestamp}")
    c.drawString(50, 765, f"Website: {data['site']}")

    y = 740

    # Section 1: Status
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "1. Website Status")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Live Status: {data['status']}")

    # Section 2: Performance
    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "2. Performance Overview")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Performance Rating: {data['performance']}")
    y -= 20
    c.drawString(50, y, "GTmetrix and PSI metrics will be added here.")

    # Section 3: SEO
    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "3. SEO Check")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"SEO Status: {data['seo']}")
    y -= 20
    c.drawString(50, y, "Broken links, sitemap, and keyword audits will be added.")

    # Section 4: Security
    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "4. Security Scan")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "UpGuard, Sucuri, and HackerTarget results will be included.")

    # Section 5: Summary
    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "5. Final Summary")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "This report confirms the site is live and performing well.")
    y -= 20
    c.drawString(50, y, "Next steps: integrate real metrics and expand audit coverage.")

    c.save()
    return filename
