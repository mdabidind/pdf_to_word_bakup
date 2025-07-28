from flask import Flask, request, send_file
import os
import uuid
from werkzeug.utils import secure_filename
from pdf2image import convert_from_path
import pytesseract
from docx import Document

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert_pdf():
    if 'pdf_file' not in request.files:
        return "No file uploaded", 400

    pdf = request.files['pdf_file']
    filename = secure_filename(pdf.filename)
    file_id = str(uuid.uuid4())
    pdf_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.pdf")
    pdf.save(pdf_path)

    images = convert_from_path(pdf_path)
    doc = Document()

    for img in images:
        text = pytesseract.image_to_string(img)
        doc.add_paragraph(text)

    doc_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.docx")
    doc.save(doc_path)

    return send_file(doc_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
