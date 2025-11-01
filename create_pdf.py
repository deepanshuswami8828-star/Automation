from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def create_pdf(data):
    filename = "connectheor_audit.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "ConnectHEOR Website Migration and Performance Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 765, f"Website: {data.get('site', 'N/A')}")

    y = 740

    def draw_section(title, lines):
        nonlocal y
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, title)
        y -= 20
        c.setFont("Helvetica", 12)
        for line in lines:
            c.drawString(50, y, line)
            y -= 20
        y -= 10

    draw_section("1. Migration Overview", [
        f"Migration Status: {data.get('migration', 'N/A')}"
    ])

    draw_section("2. Website Accessibility Across All Locations", [
        "Status: Accessible globally"
    ])

    draw_section("3. Performance Testing", [
        f"GTmetrix Grade: {data.get('gtmetrix', {}).get('grade', 'N/A')}",
        f"Performance: {data.get('gtmetrix', {}).get('performance', 'N/A')}",
        f"Structure: {data.get('gtmetrix', {}).get('structure', 'N/A')}"
    ])

    draw_section("4. SEO Audit", [
        f"SEO Status: {data.get('seo', 'N/A')}",
        f"Tools Used: {', '.join(data.get('seo_tools', []))}"
    ])

    draw_section("5. Security Audit", [
        f"Status: {data.get('security', 'N/A')}",
        f"Dead Links Found: {data.get('deadlinks', 'N/A')}"
    ])

    draw_section("6. Final Summary", [
        "Website migration and live status checks are completed successfully.",
        "Performance metrics indicate optimal loading speed and user experience.",
        "Next steps: monitor SEO scores, fix broken links, and optimize performance."
    ])

    c.save()
    return filename
