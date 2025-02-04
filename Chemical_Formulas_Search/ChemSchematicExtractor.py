import os
import cv2
import subprocess
from pdf2image import convert_from_path
from ChemSchematicExtractor import process_file

# Paths (Modify accordingly)
PDF_PATH = "research_paper.pdf"
OUTPUT_DIR = "extracted_structures"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Convert PDF to images
print("Converting PDF to images...")
pages = convert_from_path(PDF_PATH, dpi=300)

# Save each page as an image
page_images = []
for i, page in enumerate(pages):
    img_path = os.path.join(OUTPUT_DIR, f"page_{i+1}.png")
    page.save(img_path, "PNG")
    page_images.append(img_path)

# Process each page with ChemSchematicExtractor
for img_path in page_images:
    print(f"Processing: {img_path}")
    
    # Detect and extract chemical structures
    extracted_images = process_file(img_path, output_folder=OUTPUT_DIR)

    # Run OSRA on each extracted image
    for extracted_img in extracted_images:
        osra_command = f"osra -f smi {extracted_img}"
        result = subprocess.run(osra_command, shell=True, capture_output=True, text=True)
        
        # Save extracted SMILES representation
        smiles_output = result.stdout.strip()
        smiles_path = extracted_img.replace(".png", ".smi")
        with open(smiles_path, "w") as f:
            f.write(smiles_output)

        print(f"Extracted: {extracted_img} -> {smiles_output}")

print("Extraction complete. Check the extracted_structures folder.")
