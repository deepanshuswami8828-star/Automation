import json
from utils import emailer

# Load config
with open("config.json") as f:
    config = json.load(f)

# Simulate audit logic
for site in config["websites"]:
    print(f"Auditing: {site}")
    # Later: call SEO, deadlink, performance modules here

# Simulate report path
report_path = "dummy_report.pdf"

# Create a dummy file for testing
with open(report_path, "wb") as f:
    f.write(b"%PDF-1.4\n%Dummy PDF content for testing\n%%EOF")

# Send email
emailer.send(report_path, config["email"]["to"])
