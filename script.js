
function uploadPDF() {
  const input = document.getElementById('pdfInput');
  const file = input.files[0];
  const status = document.getElementById('statusMsg');
  const link = document.getElementById('downloadLink');

  if (!file) {
    status.textContent = "❌ Please select a PDF file.";
    return;
  }

  const formData = new FormData();
  formData.append("pdfFile", file);

  status.textContent = "🔄 Uploading and converting...";
  fetch("https://pdftoolslover.com/backend/upload.php", {
    method: "POST",
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === "success") {
      status.textContent = "✅ Conversion complete!";
      link.href = data.download_url;
      link.classList.remove("hidden");
    } else {
      status.textContent = "❌ Conversion failed.";
    }
  })
  .catch(err => {
    status.textContent = "❌ Error uploading file.";
    console.error(err);
  });
}
