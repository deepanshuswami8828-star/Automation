import json
from modules import seoptimer
from utils import report, emailer

# Load config
with open("config.json") as f:
    config = json.load(f)

site = config["websites"][0]
recipient = config["email"]["to"]

# 🔍 SEO Audit (SEOptimer)
seo_data = seoptimer.scan(site)

# 🚀 Performance Data (dummy for now)
performance_data = {
    "pagespeed": "Mobile: 58, Desktop: 84",
    "gtmetrix": "Performance: 61%, Structure: 81%",
    "regions": [
        {"name": "US West", "score": "41/100", "fcp": "4.6s", "lcp": "12s"},
        {"name": "Japan", "score": "53/100", "fcp": "4.9s", "lcp": "9.8s"},
        {"name": "Australia", "score": "56/100", "fcp": "5s", "lcp": "10.9s"}
    ]
}

# 🔐 Security Data (dummy for now)
security_data = {
    "findings": [
        "No malware found",
        "SSL certificate valid",
        "DeadLinkChecker: 10 broken links",
        "UpGuard: Passed",
        "Sucuri: Clean"
    ]
}

# 🧾 Generate PDF Report
report_path = report.generate(site, seo_data, performance_data, security_data)

# 📤 Send Email
emailer.send(report_path, recipient)
