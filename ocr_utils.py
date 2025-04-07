from pdf2image import convert_from_path
import pytesseract
import platform
import os
import fitz  # PyMuPDF

pytesseract.pytesseract.tesseract_cmd = "/Users/yogyach/anaconda3/envs/mediscan/bin/tesseract"

def convert_pdf_to_images(pdf_path, dpi=300):
    """
    Convert each page of a PDF into a high-resolution PIL image.

    Args:
        pdf_path (str): Path to the PDF file.
        dpi (int): Dots per inch (resolution) for image conversion.

    Returns:
        List[PIL.Image]: List of images, one per page.
    """
    return convert_from_path(pdf_path, dpi=dpi)

def extract_text_from_images(images):
    """
    Perform OCR on each image and return combined text.

    Args:
        images (List[PIL.Image]): List of page images.

    Returns:
        str: Concatenated OCR text from all pages.
    """
    full_text = ""
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        full_text += f"\n--- OCR Page {i+1} ---\n{text}"
    return full_text

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF using OCR (via image conversion).

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: OCR-extracted text.
    """
    images = convert_pdf_to_images(pdf_path)
    return extract_text_from_images(images)

def extract_text_from_pdf_direct(pdf_path):
    """
    Extract embedded text directly from a PDF using PyMuPDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted raw text without OCR.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for i, page in enumerate(doc):
        text += f"\n--- Direct Text Page {i+1} ---\n{page.get_text()}"
    doc.close()
    return text

def compare_pdf_extraction_methods(pdf_path):
    """
    Compare OCR-based and direct-text PDF parsing methods.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        dict: {
            'ocr_text': OCR-based output,
            'direct_text': text-layer output
        }
    """
    ocr_text = extract_text_from_pdf(pdf_path)
    direct_text = extract_text_from_pdf_direct(pdf_path)
    return {
        "ocr_text": ocr_text,
        "direct_text": direct_text
    }
