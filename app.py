from flask import Flask, render_template, request, send_from_directory

from modules.tech_detector import detect_tech
from modules.headers import check_headers
from modules.ssl_checker import check_ssl
from modules.port_scanner import scan_ports
from modules.owasp_checks import basic_owasp
from modules.report_generator import generate_report

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    results = None
    report = None

    if request.method == 'POST':

        url = request.form['url']

        results = {}

        results["technology"] = detect_tech(url)
        results["headers"] = check_headers(url)
        results["ssl"] = check_ssl(url)
        results["ports"] = scan_ports(url)
        results["owasp"] = basic_owasp(url)

        report = generate_report(url, results)

    return render_template(
        'index.html',
        results=results,
        report=report
    )


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('output', filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)