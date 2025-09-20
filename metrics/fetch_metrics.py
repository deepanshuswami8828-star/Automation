import requests

def fetch_psi_metrics(url, api_key):
    endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}"
    r = requests.get(endpoint)
    data = r.json()
    return {
        "performance": data["lighthouseResult"]["categories"]["performance"]["score"] * 100,
        "seo": data["lighthouseResult"]["categories"]["seo"]["score"] * 100
    }
