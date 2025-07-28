import os
import subprocess
import sys
import shutil

REQUIRED_LIBRARIES = [
    "pdf2docx", "pdf2image", "pytesseract", "pillow", "python-docx",
    "PyPDF2", "pdfminer.six", "pdfrw", "PyMuPDF", "pdfkit", "flask",
    "requests", "pyngrok"
]

REQUIRED_DIRS = ["uploads", "converted"]

def run_command(command):
    print(f"🔧 Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Failed: {command}")
        sys.exit(1)

def install_libraries():
    for lib in REQUIRED_LIBRARIES:
        run_command(f"{sys.executable} -m pip install --upgrade {lib}")

def repair_folders():
    for folder in REQUIRED_DIRS:
        if not os.path.exists(folder):
            print(f"📁 Creating folder: {folder}")
            os.makedirs(folder)

def check_wkhtmltopdf():
    wkhtml_path = shutil.which("wkhtmltopdf")
    if not wkhtml_path:
        print("⚠️ wkhtmltopdf not found! Please install from:")
        print("https://wkhtmltopdf.org/downloads.html")
    else:
        print(f"✅ wkhtmltopdf found at: {wkhtml_path}")

def update_from_github():
    if os.path.exists(".git"):
        print("🔁 Pulling latest changes from GitHub...")
        run_command("git pull")
    else:
        print("ℹ️ Git not initialized in this project. Skipping update.")

if __name__ == "__main__":
    print("🔧 Starting Update & Repair Process...")
    install_libraries()
    repair_folders()
    check_wkhtmltopdf()
    update_from_github()
    print("✅ All done!")
