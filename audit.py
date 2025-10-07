from utils import report, emailer

site = "https://connectheor.com"

seo_data = {
    "score": 84,
    "issues": ["Missing meta description", "Multiple H1 tags", "Low keyword density"]
}

performance_data = {
    "pagespeed": "Mobile: 58, Desktop: 84",
    "gtmetrix": "Performance: 61%, Structure: 81%",
    "regions": [
        {"name": "US West", "score": "41/100", "fcp": "4.6s", "lcp": "12s"},
        {"name": "Japan", "score": "53/100", "fcp": "4.9s", "lcp": "9.8s"},
        {"name": "Australia", "score": "56/100", "fcp": "5s", "lcp": "10.9s"}
    ]
}

security_data = {
    "findings": [
        "No malware found",
        "SSL certificate valid",
        "DeadLinkChecker: 10 broken links",
        "UpGuard: Passed",
        "Sucuri: Clean"
    ]
}

report_path = report.generate(site, seo_data, performance_data, security_data)
emailer.send(report_path, "kunal.hriday@connectheor.com")
