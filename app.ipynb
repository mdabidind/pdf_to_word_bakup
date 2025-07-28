# Run this in Google Colab
from flask import Flask, request, send_from_directory
from uuid import uuid4
import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from docx import Document
import shutil

!pip install --upgrade pdf2image pytesseract pillow python-docx flask pyngrok fitz pdfminer.six pdfrw pdfkit ocrmypdf

from pyngrok import ngrok

UPLOAD_DIR = '/content/uploads'
OUTPUT_DIR = '/content/output'
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf():
    file = request.files['file']
    uuid = request.form.get('uuid')
    pdf_path = f"{UPLOAD_DIR}/{uuid}.pdf"
    docx_path = f"{OUTPUT_DIR}/{uuid}.docx"

    file.save(pdf_path)

    images = convert_from_path(pdf_path)
    document = Document()

    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        document.add_paragraph(text)

    document.save(docx_path)
    return f"{public_url}/download/{uuid}.docx"

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

# Start ngrok for external access
public_url = ngrok.connect(5000).public_url
print(f"🚀 Public URL: {public_url}")

app.run(port=5000)
