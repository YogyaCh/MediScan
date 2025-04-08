from pdf2image import convert_from_path
import pytesseract
import fitz

def extract_text_from_pdf_ocr(pdf_path):
    images = convert_from_path(pdf_path)
    return "\n".join(pytesseract.image_to_string(img) for img in images)

def extract_text_from_pdf_direct(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in doc)
