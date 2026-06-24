import builtwith

def detect_tech(url):
    try:
        return builtwith.parse(url)
    except Exception as e:
        return {"error": str(e)}