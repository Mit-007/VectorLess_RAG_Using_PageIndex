from docx2pdf import convert
from reportlab.pdfgen import canvas
import os

def txt_to_pdf(txt_path, pdf_path=None):

    if pdf_path is None:
        pdf_path = txt_path.replace(".txt", ".pdf")

    c = canvas.Canvas(pdf_path)

    y = 800 

    with open(txt_path, "r", encoding="utf-8") as file:

        for line in file:
            if y < 50:
                c.showPage()
                y = 800

            c.drawString(50, y, line.strip())
            y -= 20

    c.save()

    return pdf_path

pdf_file = txt_to_pdf("input.txt")
print("PDF created at:", pdf_file)