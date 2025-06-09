import pandas as pd
import re

# Input and output file names
input_excel = 'output.xlsx'
output_txt = 'chamber_email_list.txt'

# Read the DataFrame
df = pd.read_excel(input_excel)

# Verify the columns
expected_columns = {"Name", "Email"}
if not expected_columns.issubset(df.columns):
    raise ValueError(f"The input file must have columns: {expected_columns}")

# Regex pattern to match typical email formats
email_pattern = re.compile(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}')

# We will look for emails in both columns (Name and Email)
columns_to_search = ["Name", "Email"]

all_emails = set()

for col in columns_to_search:
    for cell_value in df[col].astype(str):
        found_emails = email_pattern.findall(cell_value)
        for em in found_emails:
            all_emails.add(em.lower())  # Lowercase for consistency

# Create a comma-separated string of all emails
email_string = ", ".join(sorted(all_emails))

# Write the result to a text file
with open(output_txt, 'w', encoding='utf-8') as f:
    f.write(email_string)

print("Email list extracted and saved to", output_txt)
print("Preview:")
print(email_string[:500] + ("..." if len(email_string) > 500 else ""))
