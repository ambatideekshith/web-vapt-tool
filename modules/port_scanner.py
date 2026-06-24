import nmap
from urllib.parse import urlparse

def scan_ports(url):

    results = {}

    host = urlparse(url).hostname

    scanner = nmap.PortScanner()

    scanner.scan(hosts=host, arguments='-F')

    for host in scanner.all_hosts():

        results[host] = []

        for proto in scanner[host].all_protocols():

            ports = scanner[host][proto].keys()

            for port in ports:

                results[host].append({
                    "port": port,
                    "state": scanner[host][proto][port]['state']
                })

    return results