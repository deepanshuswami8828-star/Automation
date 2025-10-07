import requests
from bs4 import BeautifulSoup

def scan(site):
    url = f"https://www.seoptimer.com/{site.replace('https://', '').replace('http://', '')}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"score": 0, "issues": ["Failed to fetch SEOptimer data"]}

    soup = BeautifulSoup(response.text, "html.parser")

    # Try to extract score and issues (this is a placeholder — SEOptimer may change layout)
    score_tag = soup.find("div", class_="score")
    score = int(score_tag.text.strip().replace("%", "")) if score_tag else 0

    issues = []
    for li in soup.select("ul.audit-issues li"):
        issues.append(li.text.strip())

    return {"score": score, "issues": issues or ["No issues found or unable to parse"]}
