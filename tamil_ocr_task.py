import os
import pytesseract
from pdf2image import convert_from_path
from pypdf import PdfWriter
import io
import time # Added for timing
from datetime import datetime # Added for timestamps
from multiprocessing import Pool

# 1. SETUP PATHS
INPUT_DIR = r'F:\Esther\ocr\input'
OUTPUT_DIR = r'F:\Esther\ocr\output'
TESSERACT_EXE = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH = r'C:\Program Files\poppler-25.12.0\Library\bin'


pytesseract.pytesseract.tesseract_cmd = TESSERACT_EXE

def process_single_file(filename):
    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    if os.path.exists(output_path):
        return f"Skipped: {filename}"

    # Start timer for this specific file
    file_start = time.time()
    
    try:
        images = convert_from_path(input_path, dpi=250, poppler_path=POPPLER_PATH)

        writer = PdfWriter()
        
        for img in images:
            # lang='tam+eng' added to fix your English encoding issue
            page_pdf_bytes = pytesseract.image_to_pdf_or_hocr(
                            img,
                            extension='pdf',
                            lang='tam+eng',
                            config='--oem 1 --psm 6'
                        )

            writer.append(io.BytesIO(page_pdf_bytes))
            
        with open(output_path, "wb") as f:
            writer.write(f)
        
        # Calculate duration
        duration = time.time() - file_start
        return f"Done: {filename} | Time: {duration:.2f} seconds"
    
    except Exception as e:
        return f"Error in {filename}: {e}"

if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.pdf')]
    
    # Start Total Batch Timer
    batch_start_time = datetime.now()
    print(f"Batch started at: {batch_start_time.strftime('%H:%M:%S')}")
    print(f"Found {len(files)} files. Processing with 4 Workers...\n")

    with Pool(processes=4) as pool:
        results = pool.map(process_single_file, files)

    # Print individual file results
    for res in results:
        print(res)

    # Calculate Total Batch Duration
    batch_end_time = datetime.now()
    total_duration = batch_end_time - batch_start_time
    
    print("\n" + "="*50)
    print(f"BATCH COMPLETED AT: {batch_end_time.strftime('%H:%M:%S')}")
    print(f"TOTAL TIME ELAPSED: {total_duration}")
    print("="*50)