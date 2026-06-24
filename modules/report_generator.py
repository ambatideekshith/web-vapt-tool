from fpdf import FPDF
import json
import pandas as pd
import os

def generate_report(target, results):

    os.makedirs("output", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10,
             f"Web VAPT Report - {target}",
             ln=True)

    pdf.set_font("Arial", size=10)

    for section, data in results.items():

        pdf.ln(5)
        pdf.cell(0, 10, section.upper(), ln=True)

        pdf.multi_cell(0, 6, str(data))

    pdf_path = f"output/report.pdf"
    pdf.output(pdf_path)

    with open("output/report.json", "w") as f:
        json.dump(results, f, indent=4)

    df = pd.DataFrame(
        [(k, str(v)) for k, v in results.items()],
        columns=["Section", "Result"]
    )

    df.to_csv("output/report.csv", index=False)

    return pdf_path