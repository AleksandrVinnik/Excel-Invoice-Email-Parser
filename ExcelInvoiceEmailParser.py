import os
import pandas as pd
import glob
import re

def find_excel_files(root_dir):
    # Handle spaces in path by using raw string
    root_dir = r"{}".format(root_dir)
    # Find all Excel files recursively
    excel_patterns = ['*.xlsx', '*.xls']
    excel_files = []
    for pattern in excel_patterns:
        excel_files.extend(glob.glob(os.path.join(root_dir, '**', pattern), recursive=True))
    # Filter out temporary Excel files
    excel_files = [f for f in excel_files if not os.path.basename(f).startswith('~$')]
    return excel_files

def extract_emails(excel_files):
    all_emails = set()  # Using set to avoid duplicates
    # Less strict email pattern - allows more variations
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    
    total_files = len(excel_files)
    processed_files = 0
    
    for file in excel_files:
        processed_files += 1
        try:
            print(f"\rProcessing file {processed_files}/{total_files} ({processed_files/total_files*100:.1f}%) - Found {len(all_emails)} emails", end="")
            
            # Try reading with openpyxl for xlsx files
            if file.endswith('.xlsx'):
                df = pd.read_excel(file, na_filter=False, engine='openpyxl')
            # Try reading with xlrd for xls files
            else:
                df = pd.read_excel(file, na_filter=False, engine='xlrd')
            
            # Iterate through all cells in the DataFrame
            for column in df.columns:
                # Convert column to string type and search for emails
                series = df[column].astype(str)
                for cell in series:
                    # Clean the cell content
                    cell = cell.strip().lower()
                    # Skip empty or 'nan' cells
                    if cell == '' or cell == 'nan':
                        continue
                    # Find all email matches in the cell
                    emails = re.findall(email_pattern, cell)
                    # Additional validation to reduce false positives
                    valid_emails = []
                    for email in emails:
                        # Basic validation checks
                        if (len(email) >= 5 and  # Minimum length check
                            '.' in email.split('@')[1] and  # Domain has a dot
                            not email.startswith('.') and  # Doesn't start with dot
                            not email.endswith('.') and  # Doesn't end with dot
                            email.count('@') == 1):  # Exactly one @ symbol
                            valid_emails.append(email)
                    all_emails.update(valid_emails)
                
        except Exception as e:
            print(f"\nError processing {file}: {str(e)}")
            continue
    
    print("\nFinished processing all files")
    return list(all_emails)

def main():
    # Define the root directory
    root_dir = r"/Users/alvi/Documents/1. Fireplace/FIREPLACE INVOICES"
    
    # Find all Excel files
    print("Searching for Excel files...")
    excel_files = find_excel_files(root_dir)
    print(f"Found {len(excel_files)} Excel files")
    
    # Extract emails
    print("Extracting emails...")
    emails = extract_emails(excel_files)
    
    # Create DataFrame and save to CSV
    df_emails = pd.DataFrame(emails, columns=['Email'])
    output_file = os.path.join(root_dir, 'extracted_emails.csv')
    df_emails.to_csv(output_file, index=False)
    print(f"Emails saved to: {output_file}")
    print(f"Total unique emails found: {len(emails)}")

if __name__ == "__main__":
    main()
