import ssl
import socket
from urllib.parse import urlparse

def check_ssl(url):

    result = {}

    hostname = urlparse(url).hostname

    try:

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443)) as sock:

            with context.wrap_socket(
                    sock,
                    server_hostname=hostname) as ssock:

                cert = ssock.getpeercert()

                result["issuer"] = cert['issuer']
                result["expiry"] = cert['notAfter']
                result["version"] = ssock.version()

    except Exception as e:
        result["error"] = str(e)

    return result