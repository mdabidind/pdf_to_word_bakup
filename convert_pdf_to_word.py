import os
from pdf2image import convert_from_path
import pytesseract
from docx import Document
import uuid

# Setup paths
UPLOAD_FOLDER = "/content/drive/MyDrive/PDFToWordDriveTool/uploads/"
OUTPUT_FOLDER = "/content/drive/MyDrive/PDFToWordDriveTool/outputs/"

# Make sure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Convert function
def convert_pdf_to_word(file_id):
    input_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.pdf")
    output_path = os.path.join(OUTPUT_FOLDER, f"{file_id}.docx")

    images = convert_from_path(input_path)
    doc = Document()
    
    for img in images:
        text = pytesseract.image_to_string(img)
        doc.add_paragraph(text)

    doc.save(output_path)
    return output_path

# Run for a specific file
file_id = "your-unique-id-here"  # Replace via HTML upload handler
convert_pdf_to_word(file_id)
