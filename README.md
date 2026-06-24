# Web VAPT Tool

A Python-based Web Application Vulnerability Assessment and Penetration Testing (VAPT) tool developed using Flask.

## Features

* Detects web technologies used by the target website
* Checks security headers
* Performs SSL/TLS certificate analysis
* Performs basic port scanning
* Identifies common security misconfigurations
* Generates reports in:

  * PDF format
  * JSON format
  * CSV format

## Project Structure

```text
web-vapt-tool/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── tech_detector.py
│   ├── headers.py
│   ├── ssl_checker.py
│   ├── port_scanner.py
│   ├── owasp_checks.py
│   └── report_generator.py
│
├── templates/
│   └── index.html
│
├── static/
├── reports/
└── output/
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/web-vapt-tool.git
cd web-vapt-tool
```

### Install Dependencies

```bash
pip3 install -r requirements.txt
```

## Running the Application

Start the Flask application:

```bash
python3 app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Usage

1. Enter the target URL.
2. Click on **Scan**.
3. Wait for the scan to complete.
4. View the results.
5. Download reports in PDF, JSON, or CSV format.

## Sample Scan

Example target:

```text
https://example.com
```

## Technologies Used

* Python
* Flask
* Requests
* BuiltWith
* Python-Nmap
* FPDF2
* Pandas

## Disclaimer

This tool is intended for educational purposes and authorized security assessments only.

Do not scan systems, networks, or applications without explicit permission from the owner.

The author is not responsible for any misuse of this tool.

## Author

Developed by Ambati Deekshith
