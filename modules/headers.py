import requests

SEC_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

def check_headers(url):

    findings = {}

    try:
        r = requests.get(url, timeout=10)

        for header in SEC_HEADERS:

            if header in r.headers:
                findings[header] = "Present"
            else:
                findings[header] = "Missing"

    except Exception as e:
        findings["error"] = str(e)

    return findings