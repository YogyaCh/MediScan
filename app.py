import streamlit as st
from ocr_utils import compare_pdf_extraction_methods
from gpt_utils import generate_summary, answer_question
import os

st.set_page_config(layout="wide")
st.title("🧪 MediScan – Lab Report Analyzer")

uploaded_file = st.file_uploader("Upload a medical lab PDF (blood/urine)", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    method = st.radio("Select view mode:", ["Side-by-side", "OCR Only", "Direct Parsing Only"], horizontal=True)

    with st.spinner("Extracting text..."):
        results = compare_pdf_extraction_methods("temp.pdf")
        ocr_text = results["ocr_text"]
        direct_text = results["direct_text"]

    # Display extraction
    if method == "Side-by-side":
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🔍 OCR Extracted Text")
            st.text_area("OCR Output", ocr_text, height=600)
        with col2:
            st.subheader("📄 Direct PDF Text")
            st.text_area("Direct Output", direct_text, height=600)
    elif method == "OCR Only":
        st.subheader("🔍 OCR Extracted Text")
        st.text_area("OCR Output", ocr_text, height=700)
    else:
        st.subheader("📄 Direct PDF Text")
        st.text_area("Direct Output", direct_text, height=700)

    # Report type selector
    report_type = st.selectbox("What type of report is this?", ["Hematology", "Urine"], index=0)

    # Load domain knowledge
    knowledge_path = f"reference_knowledge/{report_type.lower()}_reference.txt"
    if os.path.exists(knowledge_path):
        with open(knowledge_path, "r") as f:
            knowledge = f.read()
    else:
        st.error(f"Missing knowledge file: {knowledge_path}")
        knowledge = ""

    # Generate summary
    if st.button("🧠 Generate Summary (via OpenAI)"):
        with st.spinner("Summarizing using GPT..."):
            summary = generate_summary(ocr_text, knowledge)
        st.subheader("📋 AI-Generated Summary")
        st.write(summary)

    # Optional Q&A
    question = st.text_input("Have a question about the report?")
    if question:
        with st.spinner("Getting answer..."):
            answer = answer_question(ocr_text, question, knowledge)
        st.subheader("💬 Answer")
        st.write(answer)
