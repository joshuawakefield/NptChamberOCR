# Newport Chamber of Commerce OCR Contact Extractor

### Summary

This project is an end-to-end Python pipeline that extracts structured business contact information from a copy-protected, image-based PDF directory. Faced with an intentionally non-cooperative data source, this solution automates the conversion of rasterized text into a clean, structured, and actionable dataset, demonstrating a pragmatic approach to real-world data acquisition challenges.

### Problem Statement

The Newport, RI Chamber of Commerce (politely!) declined to provide a digital copy of their member contact list. The publicly available version was a digital flyer where all text was embedded within images, preventing standard copy-pasting and data extraction. The goal was to overcome this technical barrier and produce a usable contact list.

### How It Works: The Pipeline

I engineered a multi-stage process to systematically convert the locked PDF pages into structured data.

1.  **PDF to Image Conversion:** The script first isolates the target pages (30-40, accounting for a cover offset) from the source `npt_chamber.pdf` and converts each page into a high-resolution image using the `pdf2image` library, which leverages the Poppler PDF rendering engine. 

2.  **Optical Character Recognition (OCR):** Each generated image is then processed by Google's Tesseract OCR engine via the `pytesseract` Python wrapper. This step "reads" the text from the images, turning visual data into a raw, machine-readable string. 

3.  **Parsing and Structuring:** The raw OCR text is parsed using custom logic. The script splits the text into blocks assumed to be individual business entries. Regular expressions (`regex`) are then used to pinpoint and extract specific data points like phone numbers and email addresses from the text blocks. 

4.  **Data Export:** The extracted and cleaned data (Name, Phone, Email) is structured into a `pandas` DataFrame and exported to `output.xlsx`, a universally compatible spreadsheet file. 

5.  **Post-Processing & Collation:** A second utility script, `cleaner.py`, reads the generated Excel file. It scans both the "Name" and "Email" columns for any valid email addresses that may have been misplaced during OCR, deduplicates the final list, and outputs a clean, comma-separated string to `chamber_email_list.txt` for immediate use in mail clients or marketing platforms. 

### Tech Stack

* **Core Language:** Python
* **Data Extraction & Processing:**
    * `pdf2image`: Converts PDF pages to images.
    * `Pytesseract`: Python wrapper for Google's Tesseract OCR Engine.
    * `Pandas`: For data structuring and export to Excel.
    * `re` (Regex): For robust pattern-matching and data cleaning.
* **External Dependencies:**
    * **Poppler:** A PDF rendering library required by `pdf2image`.
    * **Tesseract:** The core OCR engine.

### Key Achievements

* Successfully extracted and structured over 1,200 business contacts from a locked, image-based PDF.
* Engineered a resilient, multi-stage data pipeline from the ground up to solve a real-world data access problem.
* Demonstrated robust troubleshooting of complex environment issues, including PATH configuration for external binaries like Poppler and Tesseract. 

### Why It Matters

This project highlights an ability to diagnose problems, architect solutions, and push through technical barriers with practical tools. It’s less about a single piece of code and more about the problem-solving mindset: when the front door is locked, you build a key.
🧠 AI is a superpower—but only in the hands of those who know how to ask the right questions.

### Future Improvements

* **Layout-Aware OCR:** Integrate `layout-parser` to improve parsing accuracy by analyzing the document's visual structure.
* **Direct-to-Cloud:** Use the Google Sheets API to upload the DataFrame directly, creating a fully cloud-based workflow.
* **Web Interface:** Wrap the pipeline in a simple Flask or Streamlit app to allow users to upload their own PDFs for processing.