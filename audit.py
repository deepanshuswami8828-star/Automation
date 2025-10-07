import json
import utils.report as report
import utils.emailer as emailer
import modules.seoptimer as seoptimer

# Load config
with open("config.json") as f:
    config = json.load(f)

site = config["websites"][0]
recipient = config["email"]["to"]

# 🔍 SEO Audit
seo_data = seoptimer.scan(site)

# 🚀 Performance (dummy for now)
performance_data = {
    "pagespeed": "Mobile: 58, Desktop: 84",
    "gtmetrix": "Performance: 61%, Structure: 81%",
    "regions": [
        {"name": "US West", "score": "41/100", "fcp": "4.6s", "lcp": "12s"},
        {"name": "Japan", "score": "53/100", "fcp": "4.9s", "lcp": "9.8s"},
        {"name": "Australia", "score": "56/100", "fcp": "5s", "lcp": "10.9s"}
    ]
}

# 🔐 Security (dummy for now)
security_data = {
    "findings": [
        "No malware found",
        "SSL certificate valid",
        "DeadLinkChecker: 10 broken links",
        "UpGuard: Passed",
        "Sucuri: Clean"
    ]
}

# 🧾 Generate PDF
report_path = report.generate(site, seo_data, performance_data, security_data)

# 📤 Send Email
emailer.send(report_path, recipient)
