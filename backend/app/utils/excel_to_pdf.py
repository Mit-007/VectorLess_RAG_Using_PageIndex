import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


def excel_to_pdf(excel_path, pdf_path=None):

    if pdf_path is None:
        pdf_path = excel_path.replace(".xlsx", ".pdf")

    df = pd.read_excel(excel_path)

    data = [df.columns.tolist()] + df.values.tolist()

    pdf = SimpleDocTemplate(pdf_path)

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))

    pdf.build([table])

    return pdf_path

