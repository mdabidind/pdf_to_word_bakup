from setuptools import setup, find_packages

setup(
    name='pdf_to_word_converter',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-cors',
        'pdf2docx',
        'pytesseract',
        'pillow',
        'python-docx',
        'PyPDF2',
        'pdfminer.six',
        'pdfrw',
        'PyMuPDF',
        'pdfkit',
        'requests',
        'pyngrok'
    ],
)
