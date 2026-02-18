# Multilingual Batch OCR System for High Accuracy Digitization of Scanned PDFs

A Python-based multilingual batch OCR system designed to convert scanned PDF
documents into high-accuracy, searchable, and selectable PDFs using
Tesseract OCR and Poppler.

This project focuses on practical document digitization, especially for
scanned documents where OCR quality is often poor.

---

## 📌 Problem Statement

Many scanned PDF documents (such as books, notes, reports, and official
documents) are image-based and cannot be searched or digitally processed.
Although some scanned PDFs may allow basic search, the extracted text is
often inaccurate, incomplete, or poorly encoded.

This system addresses the need for **reliable, batch OCR processing** with
better text accuracy.

---

## 🎯 Objectives

- Convert scanned PDFs into searchable PDFs
- Support multilingual OCR (Tamil and English)
- Process multiple PDFs in batch mode
- Preserve document layout while adding a clean text layer
- Provide a simple and reusable OCR pipeline

---

## ⚙️ System Workflow
Scanned PDF
↓
Poppler (PDF → Image conversion)
↓
Tesseract OCR (Tamil / English)
↓
Searchable PDF Output


---

## 🚀 Features

- Multilingual OCR support (Tamil + English)
- Batch processing of scanned PDFs
- Searchable and selectable PDF output
- Skips already processed files automatically
- Windows-compatible implementation
- Simple folder-based input/output workflow

---

## 🛠️ Technology Stack

- **Programming Language:** Python 3.12
- **OCR Engine:** Tesseract OCR 5.x
- **PDF Processing:** Poppler, pdf2image
- **PDF Writing:** pypdf
- **Platform:** Windows

---

## 📂 Project Structure
input/ → Place scanned PDF files here

output/ → OCR-processed searchable PDFs appear here

tamil_ocr_task.py → Main OCR script


---

## ▶️ How to Run the Project

**Step 1: Install Python libraries**
```bash
pip install pytesseract pdf2image pypdf pillow

**Step 2: Install system dependencies**
Install Tesseract OCR with Tamil (tam) and English (eng) language data
Install Poppler for Windows

**Step 3: Add input PDFs**
Place all scanned PDF files inside the input/ folder.

**Step 4: Run OCR**
```bash
python tamil_ocr_task.py

**Step 5: Get output**
OCR-processed PDFs will be available in the output/ folder.






