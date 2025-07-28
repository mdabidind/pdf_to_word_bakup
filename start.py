import os
import subprocess

print("🔄 Installing or upgrading dependencies...")

subprocess.call(["pip", "install", "--upgrade", "pip"])
subprocess.call(["pip", "install", "-r", "requirements.txt"])

print("✅ All dependencies are installed.")

# Optional: Start your Flask app automatically
print("🚀 Starting the server...")
os.system("python convert.py")
