import pdfkit
from jinja2 import Environment, FileSystemLoader

def generate(site, seo_data, perf_data, sec_data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    html = template.render(
        site=site,
        seo=seo_data,
        performance=perf_data,
        security=sec_data
    )

    output_path = f"{site.replace('https://', '').replace('/', '')}_audit_report.pdf"
    pdfkit.from_string(html, output_path)
    return output_path
