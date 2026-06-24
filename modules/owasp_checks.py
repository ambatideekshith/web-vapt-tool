import requests

def basic_owasp(url):

    findings = []

    try:

        r = requests.get(url)

        if "server" in r.headers:
            findings.append(
                "Server banner disclosure detected"
            )

        if "X-Powered-By" in r.headers:
            findings.append(
                "Technology disclosure detected"
            )

        if "autocomplete" in r.text:
            findings.append(
                "Review forms for autocomplete usage"
            )

    except Exception as e:
        findings.append(str(e))

    return findings