import os
import uuid
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from pdf2docx import Converter

app = Flask(__name__)
app.debug = True
app.config['PROPAGATE_EXCEPTIONS'] = True

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
OUTPUT_FOLDER = os.path.join(os.getcwd(), 'converted')

# Create necessary folders
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '✅ PDF to Word API is running.'

@app.route('/convert', methods=['POST'])
def convert_pdf():
    try:
        if 'pdf' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'}), 400

        file = request.files['pdf']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'Empty filename'}), 400

        filename = secure_filename(file.filename)
        file_id = str(uuid.uuid4())
        pdf_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.pdf")
        docx_path = os.path.join(OUTPUT_FOLDER, f"{file_id}.docx")

        file.save(pdf_path)
        print(f"📥 PDF uploaded to: {pdf_path}")

        try:
            converter = Converter(pdf_path)
            converter.convert(docx_path, start=0, end=None)
            converter.close()
            print(f"✅ Successfully converted to: {docx_path}")
        except Exception as conv_err:
            print(f"❌ Conversion failed: {conv_err}")
            return jsonify({'success': False, 'error': 'Conversion failed'}), 500

        return jsonify({'success': True, 'file_id': file_id})

    except Exception as e:
        print(f"❌ Server error: {e}")
        return jsonify({'success': False, 'error': 'Internal server error'}), 500


@app.route('/converted/<file_id>.docx', methods=['GET'])
def download_file(file_id):
    docx_path = os.path.join(OUTPUT_FOLDER, f"{file_id}.docx")
    if os.path.exists(docx_path):
        return send_file(docx_path, as_attachment=True)
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
