from pdfminer.high_level import extract_text
import docx
import re

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    print("\nExtracted Emails:", emails)  # Debugging output
    return emails[0] if emails else None

def extract_phone(text):
    pattern = r"\+?\d{1,4}[\s-]?\(?\d{2,3}\)?[\s-]?\d{3,4}[\s-]?\d{4}"
    phones = re.findall(pattern, text)
    print("\nExtracted Phone Numbers:", phones)  # Debugging output
    return phones[0] if phones else None

def extract_name(text):
    match = re.search(r'[A-Za-z]+ [A-Za-z]+', text)
    return match.group(0) if match else None