from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf(data):
    filename = "connectheor_audit.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, f"Website Audit Report: {data['site']}")
    c.setFont("Helvetica", 12)

    y = 770
    c.drawString(50, y, f"Status: {data['status']}")
    y -= 20
    c.drawString(50, y, f"Migration: {data['migration']}")

    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Performance Metrics")
    c.setFont("Helvetica", 12)
    y -= 20
    c.drawString(50, y, f"GTmetrix Grade: {data['performance']['GTmetrix']['grade']}")
    y -= 20
    c.drawString(50, y, f"LCP: {data['performance']['GTmetrix']['LCP']}, TBT: {data['performance']['GTmetrix']['TBT']}, CLS: {data['performance']['GTmetrix']['CLS']}")
    y -= 20
    c.drawString(50, y, f"PageSpeed Insights - Mobile: {data['performance']['PageSpeed Insights']['mobile']}, Desktop: {data['performance']['PageSpeed Insights']['desktop']}")

    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Global Accessibility Scores")
    c.setFont("Helvetica", 12)
    for region, score in data["accessibility"].items():
        y -= 20
        c.drawString(50, y, f"{region}: {score}")

    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Security Audit")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, data["security"])

    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Broken Links")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Total broken links found: {data['broken_links']}")

    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Sitemap & SEO Audit")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, data["sitemap"])

    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Final Summary")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, data["summary"])

    c.save()
    return filename
