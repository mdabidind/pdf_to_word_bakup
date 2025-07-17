
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['pdfFile'])) {
    $uploadDir = __DIR__ . '/output/';
    $fileName = uniqid() . '_' . basename($_FILES['pdfFile']['name']);
    $uploadFile = $uploadDir . $fileName;

    if (move_uploaded_file($_FILES['pdfFile']['tmp_name'], $uploadFile)) {
        // Simulate conversion (rename to .docx)
        $wordFile = $uploadDir . pathinfo($fileName, PATHINFO_FILENAME) . '.docx';
        copy($uploadFile, $wordFile);

        $downloadUrl = "https://pdftoolslover.com/backend/output/" . basename($wordFile);
        echo json_encode(["status" => "success", "download_url" => $downloadUrl]);
    } else {
        echo json_encode(["status" => "error", "message" => "Upload failed"]);
    }
} else {
    echo json_encode(["status" => "error", "message" => "Invalid request"]);
}
?>
