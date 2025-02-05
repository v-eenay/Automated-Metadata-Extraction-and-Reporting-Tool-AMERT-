import os
import zipfile
from datetime import datetime
from pikepdf import Pdf, PdfError
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
from docx import Document
from openpyxl import Workbook

# Constants for folder and file paths
SUBMISSIONS_FOLDER = "submissions"
EXTRACTED_FOLDER = "extracted"
OUTPUT_EXCEL_FILE = "metadata.xlsx"

# Function to extract the name from the folder name
def extract_name_from_folder(folder_name):
    # Split folder name by underscore and extract first and last name
    parts = folder_name.split("_")
    if len(parts) >= 2:
        firstname, lastname = parts[0], parts[1]
        return f"{firstname} {lastname}"
    return "N/A"  # Return "N/A" if name cannot be extracted

# Function to parse date strings into datetime objects
def parse_date(date_str):
    if not date_str:  # If the date string is empty, return None
        return None
    try:
        # Convert pikepdf.String to a regular Python string
        date_str = str(date_str)
        
        # Handle 'D:' prefix in PDF dates
        if date_str.startswith("D:"):
            date_str = date_str[2:]
        
        # Parse the first 14 characters (YYYYMMDDHHMMSS)
        parsed_date = datetime.strptime(date_str[:14], '%Y%m%d%H%M%S')
        print(f"Parsed date successfully: {parsed_date}")  # Log successful parsing
        return parsed_date
    except ValueError as e:
        print(f"Error parsing date '{date_str}': {e}")  # Log parsing errors
        return None  # Return None if parsing fails

# Function to extract metadata using pikepdf
def get_pdf_metadata_pikepdf(file_path):
    try:
        with Pdf.open(file_path) as pdf:
            metadata = pdf.docinfo
            print(f"Extracted metadata using pikepdf: {metadata}")  # Log extracted metadata
            
            creation_date = parse_date(metadata.get('/CreationDate', '')) if '/CreationDate' in metadata else None
            modification_date = parse_date(metadata.get('/ModDate', '')) if '/ModDate' in metadata else None
            
            edit_time = (
                (modification_date - creation_date).total_seconds() / 60
                if creation_date and modification_date
                else "N/A"
            )
            
            return {
                "Author": str(metadata.get('/Author', "N/A")),
                "Title": str(metadata.get('/Title', "N/A")),
                "Creator": str(metadata.get('/Creator', "N/A")),
                "Producer": str(metadata.get('/Producer', "N/A")),
                "Edit Time (minutes)": edit_time,
            }
    except PdfError as e:
        print(f"pikepdf failed to read file {file_path}: {e}")  # Log pikepdf errors
        return None  # Return None if pikepdf fails to read the file

# Function to extract metadata using PyPDF2
def get_pdf_metadata_pypdf2(file_path):
    try:
        reader = PdfReader(file_path)
        metadata = reader.metadata
        print(f"Extracted metadata using PyPDF2: {metadata}")  # Log extracted metadata
        
        creation_date = parse_date(metadata.get("/CreationDate")) if metadata else None
        modification_date = parse_date(metadata.get("/ModDate")) if metadata else None
        
        edit_time = (
            (modification_date - creation_date).total_seconds() / 60
            if creation_date and modification_date
            else "N/A"
        )
        
        return {
            "Author": metadata.get("/Author", "N/A") if metadata else "N/A",
            "Title": metadata.get("/Title", "N/A") if metadata else "N/A",
            "Creator": metadata.get("/Creator", "N/A") if metadata else "N/A",
            "Producer": metadata.get("/Producer", "N/A") if metadata else "N/A",
            "Edit Time (minutes)": edit_time,
        }
    except PdfReadError as e:
        print(f"PyPDF2 failed to read file {file_path}: {e}")  # Log PyPDF2 errors
        return None  # Return None if PyPDF2 fails to read the file
    except Exception as e:
        print(f"Unexpected error reading file {file_path}: {e}")  # Log unexpected errors
        return None  # Catch any other unexpected errors

# Combined function to extract PDF metadata using both libraries
def get_pdf_metadata(file_path):
    metadata = get_pdf_metadata_pikepdf(file_path)
    if metadata is None:
        metadata = get_pdf_metadata_pypdf2(file_path)
    if metadata:
        print(f"Successfully extracted metadata for file: {file_path}")  # Log success
    else:
        print(f"Failed to extract metadata for file: {file_path}")  # Log failure
    return metadata or {
        "Author": "N/A",
        "Title": "N/A",
        "Creator": "N/A",
        "Producer": "N/A",
        "Edit Time (minutes)": "N/A",
    }

# Function to extract metadata from DOCX files
def get_docx_metadata(file_path):
    try:
        doc = Document(file_path)
        core_properties = doc.core_properties
        print(f"Extracted metadata from DOCX file: {file_path}")  # Log extracted metadata
        
        creation_date = core_properties.created
        modification_date = core_properties.modified
        
        edit_time = (
            (modification_date - creation_date).total_seconds() / 60
            if creation_date and modification_date
            else "N/A"
        )
        
        return {
            "Author": core_properties.author or "N/A",
            "Title": core_properties.title or "N/A",
            "Creator": "N/A",
            "Producer": "N/A",
            "Edit Time (minutes)": edit_time,
        }
    except Exception as e:
        print(f"Error reading DOCX file {file_path}: {e}")  # Log DOCX errors
        return {
            "Author": "N/A",
            "Title": "N/A",
            "Creator": "N/A",
            "Producer": "N/A",
            "Edit Time (minutes)": "N/A",
        }

# Function to scan the extracted folder and extract metadata
def scan_and_extract_metadata(folder):
    metadata_list = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.startswith("._"):  # Skip macOS hidden files
                continue
            file_path = os.path.join(root, file)
            # Extract the name of the main folder inside the "extracted" folder
            submitted_by = os.path.basename(os.path.dirname(root))
            if file.endswith(".pdf"):  # Process PDF files
                metadata = get_pdf_metadata(file_path)
                metadata["File"] = os.path.basename(file_path)  # Store only the filename
                metadata["Type"] = "PDF"
                metadata["Submitted By"] = submitted_by
                metadata_list.append(metadata)
            elif file.endswith(".docx"):  # Process DOCX files
                metadata = get_docx_metadata(file_path)
                metadata["File"] = os.path.basename(file_path)  # Store only the filename
                metadata["Type"] = "DOCX"
                metadata["Submitted By"] = submitted_by
                metadata_list.append(metadata)
            else:
                print(f"Skipping unsupported file type: {file_path}")  # Log unsupported files
    return metadata_list

# Function to write metadata to an Excel file
def write_metadata_to_excel(metadata_list, output_file):
    wb = Workbook()
    ws = wb.active
    ws.title = "Metadata"
    headers = [
        "Submitted By", "File", "Type", "Author", "Title", "Creator", "Producer", "Edit Time (minutes)"
    ]
    ws.append(headers)  # Add headers to the worksheet
    for metadata in metadata_list:
        row = []
        for header in headers:
            value = metadata.get(header, "N/A")
            # Convert datetime objects to strings
            if isinstance(value, datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            # Convert floats to integers if they are whole numbers
            elif isinstance(value, float) and value.is_integer():
                value = int(value)
            # Ensure all values are strings to avoid Excel conversion errors
            row.append(str(value))
        try:
            ws.append(row)  # Add the row to the worksheet
        except Exception as e:
            print(f"Error appending row to Excel: {e}, Row: {row}")  # Log Excel errors
    try:
        wb.save(output_file)  # Save the workbook to the output file
        print(f"Metadata successfully written to {output_file}")  # Log success
    except Exception as e:
        print(f"Error saving Excel file: {e}")  # Log Excel save errors

# Function to extract all zip files in the submissions folder
def extract_zip_files(submissions_folder, extracted_folder):
    if not os.path.exists(extracted_folder):  # Create the extracted folder if it doesn't exist
        os.makedirs(extracted_folder)
    for root, _, files in os.walk(submissions_folder):
        for file in files:
            if file.endswith(".zip"):  # Process only zip files
                zip_path = os.path.join(root, file)
                extract_path = os.path.join(extracted_folder, os.path.splitext(file)[0])
                print(f"Extracting: {zip_path} to {extract_path}")  # Log extraction process
                try:
                    os.makedirs(extract_path, exist_ok=True)  # Ensure the target directory exists
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_path)
                    print(f"Successfully extracted {zip_path}")  # Log success
                except FileNotFoundError as e:
                    print(f"Error extracting {zip_path}: {e}")  # Log extraction errors
                except Exception as e:
                    print(f"Unexpected error extracting {zip_path}: {e}")  # Log unexpected errors

# Main function to orchestrate the script
def main():
    print("Starting script...")  # Log script start
    # Step 1: Extract all zip files
    print("Extracting zip files...")
    extract_zip_files(SUBMISSIONS_FOLDER, EXTRACTED_FOLDER)
    
    # Step 2: Scan the extracted folder and extract metadata
    print("Scanning extracted folder for metadata...")
    metadata_list = scan_and_extract_metadata(EXTRACTED_FOLDER)
    
    # Step 3: Write the metadata to an Excel file
    print("Writing metadata to Excel file...")
    write_metadata_to_excel(metadata_list, OUTPUT_EXCEL_FILE)
    print("Script completed successfully.")  # Log script completion

# Entry point of the script
if __name__ == "__main__":
    main()