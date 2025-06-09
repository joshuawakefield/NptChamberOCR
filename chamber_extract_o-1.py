import re
import pandas as pd
import pytesseract
from pdf2image import convert_from_path

# -------------------------------
# Configuration
# -------------------------------
pdf_path = 'npt_chamber.pdf'
output_excel = 'output.xlsx'

# Desired pages: 28-38 (due to cover offset, actual pages are 30-40)
# pdf2image page numbering starts at 1 (like humans, not zero-based).
# So, specifying first_page=30 and last_page=40 will get pages 30 to 40 inclusive.
first_page = 30
last_page = 40

# Regex patterns to identify phone and email
phone_pattern = re.compile(r'\(\d{3}\)\s?\d{3}-\d{4}')
email_pattern = re.compile(r'@')

# -------------------------------
# Step 1: Convert PDF pages to Images
# -------------------------------
print(f"Converting pages {first_page} to {last_page} of {pdf_path} into images...")
pages = convert_from_path(pdf_path, dpi=200, first_page=first_page, last_page=last_page)
print(f"Number of images generated: {len(pages)}")

# -------------------------------
# Step 2: OCR each image to extract text
# -------------------------------
all_text = ""
for i, page_image in enumerate(pages, start=first_page):
    # OCR the image using pytesseract
    print(f"\nPerforming OCR on page {i}...")
    text = pytesseract.image_to_string(page_image)
    text_length = len(text)
    print(f"Extracted text length from page {i}: {text_length} characters")
    # Print a snippet for verification
    if text_length > 0:
        print("Text snippet:")
        print(text[:200], "\n", "-"*40)
    else:
        print("No text extracted. This page may have poor image quality for OCR or no text.")

    # Combine all pages' text
    all_text += "\n" + text

# -------------------------------
# Step 3: Parse the extracted text into entries
# We assume each business block is separated by blank lines.
# -------------------------------
print("\nParsing entries from the OCR text...")
entries = re.split(r'\n\s*\n+', all_text.strip())
print(f"Number of entries found: {len(entries)}")

# -------------------------------
# Function to extract fields (Name, Phone, Email) from an entry
# -------------------------------
def extract_fields_from_entry(entry_text):
    lines = [line.strip() for line in entry_text.split('\n') if line.strip()]

    if not lines:
        print("No lines found in this entry.")
        return "", "", ""

    # The first line is the Business Name
    name = lines[0]
    phone = ""
    email = ""

    # Check remaining lines for phone and email
    for line in lines[1:]:
        # Check phone
        if phone_pattern.search(line):
            phone = line
            print(f"Phone found: {phone}")
        # Check email
        if email_pattern.search(line):
            # Extract the first token that contains '@'
            email_candidates = [word for word in line.split() if '@' in word]
            if email_candidates:
                email = email_candidates[0]
                print(f"Email found: {email}")

        # If we have both, no need to continue searching
        if phone and email:
            break

    return name, phone, email

# -------------------------------
# Step 4: Extract data for each entry and build a list of dictionaries
# -------------------------------
data = []
for i, entry in enumerate(entries, start=1):
    print(f"\nProcessing Entry {i}:")
    # Show a snippet of the entry
    print(entry[:300] + ('...' if len(entry) > 300 else ''))

    name, phone, email = extract_fields_from_entry(entry)
    print(f"Extracted -> Name: {name}, Phone: {phone}, Email: {email}")

    # Only add if there's at least a business name
    if name.strip():
        data.append({
            "Name": name,
            "Phone": phone,
            "Email": email
        })
    else:
        print("Skipping this entry as no valid name was found.")

# -------------------------------
# Step 5: Save the extracted data to an Excel file
# -------------------------------
if not data:
    print("No data entries extracted. The Excel file would be empty.")
else:
    print(f"\nTotal records extracted: {len(data)}")

df = pd.DataFrame(data, columns=["Name", "Phone", "Email"])
df.to_excel(output_excel, index=False)
print(f"Data successfully extracted and saved to {output_excel}")
