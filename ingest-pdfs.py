import pytesseract
from pytesseract import Output
import pandas as pd
import re

def process_pages(pdf_path, start_page, end_page):
    hymns = []

    for i in range(start_page, end_page):
        images = convert_from_path(pdf_path, first_page=i+1, last_page=i+1)
        for image in images:
            # Apply OCR to the image
            text = pytesseract.image_to_string(image, config='--psm 6', lang='eng')

            # Check if the page contains a hymn
            match = re.search(r'Hymn (\d+)', text)
            if match:
                hymn_number = match.group(1)
                hymns.append({'Hymn Number': hymn_number, 'Text': text})

    return hymns

hymns = process_pages(pdf_path, 0, 10)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(hymns)

# Save the DataFrame to a CSV file
df.to_csv("/mnt/data/hymns.csv", index=False)

df.head()