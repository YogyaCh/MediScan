from core import extractor

def test_direct_pdf_extraction():
    text = extractor.extract_text_from_pdf_direct("tests/sample_report_blood.pdf")
    assert "HAEMOGLOBIN" in text

def test_ocr_extraction():
    text = extractor.extract_text_from_pdf_ocr("tests/sample_report_blood.pdf")
    assert len(text) > 100