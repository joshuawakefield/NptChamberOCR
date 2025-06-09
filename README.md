# Newport Chamber of Commerce OCR Contact Extractor

## Summary
This project showcases an AI-assisted pipeline for extracting structured business contact information from a publicly visible—but intentionally copy-protected—chamber of commerce directory PDF. The original source was an image-based, non-interactive digital flyer, which required advanced processing to convert into usable, structured data.

## Problem Statement
The Newport, RI Chamber of Commerce declined to provide their member contact list, despite the list being publicly viewable online. The information was embedded in images to prevent direct copying, complicating any attempt at data extraction.

## My Approach
Rather than accept this as a dead end, I viewed it as a technical challenge. My engineering brain went to work. With no selectable text and over a dozen pages of image-encoded content, I built a resilient data extraction pipeline using OCR and regular expression parsing.

- **Image Conversion**: Used `pdf2image` to convert specific PDF pages (30–40) to raster images.
- **Optical Character Recognition (OCR)**: Extracted text from images using `pytesseract`, providing a viable path for machine-readable content.
- **Regex-based Parsing**: Developed pattern-matching logic to isolate names, emails, and phone numbers.
- **Data Structuring**: Employed pandas to clean and format the extracted information into a usable Excel file.
- **Post-Processing**: Created a standalone utility to extract and de-duplicate valid emails into a separate file.

## Key Achievements
- Extracted over **1,200 business contacts** from a non-cooperative data source.
- Produced clean, spreadsheet-ready contact lists usable in marketing, analytics, or CRM tools.
- Demonstrated **pragmatic AI integration** with traditional scripting—mixing large language model guidance with classical programming methods.

## Tools & Technologies
- `Python`, `pandas`, `pytesseract`, `pdf2image`
- Regex for robust pattern extraction
- Markdown documentation and structured comments for technical transparency

## Why It Matters
This project highlights my ability to reverse-engineer real-world constraints, integrate AI tools fluidly, and push through institutional barriers with practical technical solutions. It’s less about the code, and more about the mindset.

> 🧠 *AI is a superpower—but only in the hands of those who know how to ask the right questions.*

## Future Improvements
- Use `layoutparser` or `OCRmyPDF` for layout-aware extraction.
- Integrate Google Sheets API for direct cloud syncing.
- Wrap the pipeline into a Flask or Streamlit app for reusability.