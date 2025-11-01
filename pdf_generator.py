from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime
import os

def create_pdf(data):
    filename = "connectheor_audit.pdf"
    c = canvas.Canvas(filename, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "ConnectHEOR Website Migration and Performance Report")
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 765, f"Website: {data['site']}")

    y = 740
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "1. Migration Overview")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Migration Status: {data.get('migration', 'N/A')}")
    y -= 150
    if os.path.exists("assets/migration.png"):
        c.drawImage(ImageReader("assets/migration.png"), 50, y, width=500, height=120)

    # Add more sections here...

    c.save()
    return filename
