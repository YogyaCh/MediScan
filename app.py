import streamlit as st
from ocr_utils import compare_pdf_extraction_methods

st.set_page_config(layout="wide")
st.title("📄 PDF Text Extraction Comparison Tool")

st.markdown("Upload a PDF and compare **OCR vs Direct Parsing** side by side.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    method = st.radio(
        "Select view mode:",
        ["Side-by-side", "OCR Only", "Direct Parsing Only"],
        horizontal=True
    )

    with st.spinner("Extracting text..."):
        results = compare_pdf_extraction_methods("temp.pdf")

    if method == "Side-by-side":
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🔍 OCR Extracted Text")
            st.text_area("OCR Output", results["ocr_text"], height=600)

        with col2:
            st.subheader("📄 Direct PDF Text")
            st.text_area("Direct Text Output", results["direct_text"], height=600)

    elif method == "OCR Only":
        st.subheader("🔍 OCR Extracted Text")
        st.text_area("OCR Output", results["ocr_text"], height=700)

    else:
        st.subheader("📄 Direct PDF Text")
        st.text_area("Direct Text Output", results["direct_text"], height=700)
