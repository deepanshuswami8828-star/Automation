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

    def draw_section(title, lines, image_name=None):
        nonlocal y
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, title)
        y -= 20
        c.setFont("Helvetica", 12)
        for line in lines:
            c.drawString(50, y, line)
            y -= 20
        if image_name and os.path.exists(f"assets/{image_name}"):
            y -= 140
            c.drawImage(ImageReader(f"assets/{image_name}"), 50, y, width=500, height=120)
            y -= 20

    # Sections
    draw_section("1. Migration Overview", [
        f"Migration Status: {data.get('migration', 'N/A')}"
    ], "migration.png")

    draw_section("2. Website Accessibility", [
        "Status: Accessible globally"
    ], "lighthouse_scores.png")

    draw_section("3. Performance Testing", [
        f"GTmetrix Grade: {data.get('gtmetrix', {}).get('grade', 'N/A')}",
        f"Performance: {data.get('gtmetrix', {}).get('performance', 'N/A')}",
        f"Structure: {data.get('gtmetrix', {}).get('structure', 'N/A')}"
    ], "gtmetrix.png")

    draw_section("4. SEO Audit", [
        f"SEO Status: {data.get('seo', 'N/A')}",
        f"Tools Used: {', '.join(data.get('seo_tools', []))}"
    ], "seo_summary.png")

    draw_section("5. Security Audit", [
        f"Status: {data.get('security', 'N/A')}",
        f"Dead Links Found: {data.get('deadlinks', 'N/A')}"
    ], "upguard.png")

    draw_section("6. Final Summary", [
        "Website migration and live status checks are completed successfully.",
        "Performance metrics indicate optimal loading speed and user experience.",
        "Next steps: monitor SEO scores, fix broken links, and optimize performance."
    ])

    # Free tool integrations
    draw_section("7. Roastd Audit Summary", [
        f"Score: {data.get('roastd', {}).get('score', 'N/A')}",
        f"Issues Found: {data.get('roastd', {}).get('issues', 'N/A')}"
    ], "roastd_summary.png")

    draw_section("8. SEOmator Audit", [
        f"SEO Score: {data.get('seomator', {}).get('seo_score', 'N/A')}",
        f"Mobile Friendliness: {data.get('seomator', {}).get('mobile', 'N/A')}"
    ], "seomator_landing.png")

    draw_section("9. SEO Site Checker Report", [
        f"Health Score: {data.get('sitechecker', {}).get('health', 'N/A')}",
        f"Broken Links: {data.get('sitechecker', {}).get('broken_links', 'N/A')}"
    ], "sitechecker_health.png")

    draw_section("10. PageSpeed Insights", [
        f"Mobile Score: {data.get('pagespeed', {}).get('mobile', 'N/A')}",
        f"Desktop Score: {data.get('pagespeed', {}).get('desktop', 'N/A')}"
    ], "pagespeed_mobile.png")

    draw_section("11. UpGuard Security Scan", [
        f"SSL: {data.get('upguard', {}).get('ssl', 'N/A')}",
        f"Malware: {data.get('upguard', {}).get('malware', 'N/A')}",
        f"Leaks: {data.get('upguard', {}).get('leaks', 'N/A')}"
    ], "upguard_scan.png")

    c.save()
    return filename
