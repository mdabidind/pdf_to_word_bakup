// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  console.log('✅ Website Loaded');

  const form = document.getElementById('uploadForm');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const fileInput = document.getElementById('pdfFile');
      const statusMsg = document.getElementById('statusMsg');
      const downloadLink = document.getElementById('downloadLink');

      if (!fileInput || !fileInput.files.length) {
        alert('Please select a PDF file to convert.');
        return;
      }

      const formData = new FormData();
      formData.append('pdf', fileInput.files[0]);

      // Optional: Show uploading message
      if (statusMsg) statusMsg.textContent = '⏳ Uploading and converting...';

      try {
        // CHANGE THIS URL to your backend endpoint (e.g., Replit or Python server)
        const backendURL = 'https://your-python-backend-url/convert'; // <-- Update this

        const response = await fetch(backendURL, {
          method: 'POST',
          body: formData,
        });

        const result = await response.json();

        if (result.success) {
          if (statusMsg) statusMsg.textContent = '✅ Conversion successful!';
          downloadLink.href = result.download_url; // result.download_url must be returned by Flask
          downloadLink.style.display = 'block';
        } else {
          if (statusMsg) statusMsg.textContent = '❌ Conversion failed: ' + result.error;
          downloadLink.style.display = 'none';
        }
      } catch (err) {
        console.error(err);
        if (statusMsg) statusMsg.textContent = '⚠️ Server error. Conversion failed.';
        downloadLink.style.display = 'none';
      }
    });
  }
});
