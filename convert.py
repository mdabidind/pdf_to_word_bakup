#!/usr/bin/env python3

from flask import Flask, request, send_file
import os
import tempfile
import uuid
from pdf2image import convert_from_path
import pytesseract
from docx import Document

app = Flask(__name__)

@app.route('/convert.py', methods=['POST'])
def convert_pdf():
    if 'pdf_file' not in request.files:
        return "No file uploaded", 400

    pdf_file = request.files['pdf_file']
    temp_dir = tempfile.mkdtemp()
    pdf_path = os.path.join(temp_dir, "input.pdf")
    output_path = os.path.join(temp_dir, "output.docx")
    pdf_file.save(pdf_path)

    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=300)
    document = Document()

    for i, img in enumerate(images):
        text = pytesseract.image_to_string(img)
        document.add_paragraph(text)

    document.save(output_path)
    return send_file(output_path, as_attachment=True, download_name="converted.docx")

if __name__ == '__main__':
    app.run()
