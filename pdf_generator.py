from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf(data):
    filename = "connectheor_audit.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica", 14)
    c.drawString(100, 800, f"Website Audit Report: {data['site']}")
    c.drawString(100, 770, f"Status: {data['status']}")
    c.drawString(100, 740, f"Performance: {data['performance']}")
    c.drawString(100, 710, f"SEO: {data['seo']}")
    c.save()
    return filename
