// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  console.log('✅ Website Loaded');

  // Example: Handle form submission
  const form = document.getElementById('uploadForm');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const fileInput = document.getElementById('pdfFile');
      if (!fileInput || !fileInput.files.length) {
        alert('Please select a PDF file to convert.');
        return;
      }

      const formData = new FormData();
      formData.append('pdf', fileInput.files[0]);

      try {
        // Send to backend for conversion
        const response = await fetch('/convert', {
          method: 'POST',
          body: formData,
        });

        const result = await response.json();

        if (result.success) {
          // Show download link
          const downloadLink = document.getElementById('downloadLink');
          downloadLink.href = `/converted/${result.file_id}.docx`;
          downloadLink.style.display = 'block';
        } else {
          alert('❌ Conversion failed: ' + result.error);
        }

      } catch (err) {
        console.error(err);
        alert('⚠️ An error occurred during conversion.');
      }
    });
  }
});
