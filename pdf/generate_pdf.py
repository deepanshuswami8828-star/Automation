from fpdf import FPDF

def generate_pdf(report_data, filename="audit_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for url, metrics in report_data.items():
        pdf.cell(200, 10, txt=f"Audit for {url}", ln=True)
        for key, value in metrics.items():
            pdf.cell(200, 10, txt=f"{key.capitalize()}: {value}", ln=True)
    pdf.output(filename)
