import os
import cv2
import numpy as np
from pdf2image import convert_from_path
from PIL import Image

# === CONFIG ===
PDF_PATH = "paper2.pdf"  # Path to the PDF file
OUTPUT_DIR = "output_structures"  # Directory to save cropped images
DPI = 300  # Resolution for PDF conversion

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Convert PDF pages to images
print("[INFO] Converting PDF to images...")
pages = convert_from_path(PDF_PATH, dpi=DPI)

for page_num, page in enumerate(pages):
    print(f"[INFO] Processing page {page_num + 1}...")

    # Convert PIL image to OpenCV format
    image = np.array(page)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process detected contours
    structure_count = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        # Filter out small detections (adjust threshold as needed)
        if w > 50 and h > 50:
            cropped = image[y:y+h, x:x+w]

            # Save cropped image
            output_path = os.path.join(OUTPUT_DIR, f"page_{page_num+1}_structure_{structure_count}.png")
            cv2.imwrite(output_path, cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR))
            structure_count += 1

    print(f"[INFO] Extracted {structure_count} structures from page {page_num + 1}")

print("[INFO] Extraction complete. Check the output directory.")
