import streamlit as st
import os
import openai

from core.extractor import extract_text_from_pdf_ocr, extract_text_from_pdf_direct
from core.knowledge_loader import load_knowledge
from core.summarizer import generate_summary, answer_question
from utils.logger import logger

st.set_page_config(layout="wide")
st.title("🧪 MediScan – Lab Report Analyzer")

uploaded_file = st.file_uploader("📄 Upload a medical lab PDF (blood/urine)", type=["pdf"])

if uploaded_file:
    # Save the uploaded PDF to temp
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    logger.info("PDF uploaded successfully: temp.pdf")
    st.success("PDF uploaded and saved successfully!")

    # Extraction mode selector
    method = st.radio("🧰 Extraction Method", ["Side-by-side", "OCR Only", "Direct Parsing Only"], horizontal=True)

    with st.spinner("🔍 Extracting text from PDF..."):
        ocr_text = extract_text_from_pdf_ocr("temp.pdf")
        direct_text = extract_text_from_pdf_direct("temp.pdf")

    # Button to toggle visibility
    if st.button("🔍 Show Extracted Text"):
        logger.info(f"User clicked to view extracted text using method: {method}")

        if method == "Side-by-side":
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("🖼 OCR Extracted Text")
                st.text_area("OCR Output", ocr_text, height=600)
                logger.info("Displayed OCR text in side-by-side mode.")
            with col2:
                st.subheader("📄 Direct Parsed Text")
                st.text_area("Direct Output", direct_text, height=600)
                logger.info("Displayed Direct text in side-by-side mode.")
        elif method == "OCR Only":
            st.subheader("🖼 OCR Extracted Text")
            st.text_area("OCR Output", ocr_text, height=700)
            logger.info("Displayed OCR-only text.")
        else:
            st.subheader("📄 Direct Parsed Text")
            st.text_area("Direct Output", direct_text, height=700)
            logger.info("Displayed Direct-only text.")
    
    logger.info(f"User chose extraction method: {method}, but has not viewed the text yet.")


    # Select report type
    report_type = st.selectbox("📑 What type of report is this?", ["Hematology", "Urine"], index=0)

    knowledge = load_knowledge(report_type)

    # Option to choose input source for GPT
    use_ocr_input = st.checkbox("Use OCR output for GPT summary?", value=True)
    input_text = ocr_text if use_ocr_input else direct_text

    # Generate Summary
    if st.button("🧠 Generate Summary"):
        with st.spinner("Calling OpenAI..."):
            try:
                summary = generate_summary(input_text, knowledge)
                logger.info(f"✅ Summary generated for {report_type} report.")
                st.subheader("📋 AI-Generated Summary")
                st.write(summary)

            except openai.OpenAIError as e:
                logger.error(f"❌ OpenAI Summary Failed: {e}")
                if "429" in str(e) or "quota" in str(e).lower():
                    st.error("⚠️ You have exceeded your current OpenAI quota. Please check your API usage and billing plan.")
                else:
                    st.error("Something went wrong while generating the summary. Please try again later.")
            except Exception as e:
                logger.exception("Unhandled exception during summary generation.")
                st.error("Unexpected error while generating summary.")

    # Optional Q&A
    question = st.text_input("💬 Have a question about the report?")
    if question:
        with st.spinner("Calling OpenAI..."):
            try:
                answer = answer_question(input_text, question, knowledge)
                logger.info("✅ Q&A response successfully generated.")
                st.subheader("💡 Answer")
                st.write(answer)

            except openai.OpenAIError as e:
                logger.error(f"❌ OpenAI Q&A Failed: {e}")
                if "429" in str(e) or "quota" in str(e).lower():
                    st.error("⚠️ Your OpenAI API quota has been exceeded. Please verify your plan and usage limits.")
                else:
                    st.error("Something went wrong while answering the question.")
            except Exception as e:
                logger.exception("Unhandled exception during Q&A.")
                st.error("Unexpected error while answering the question.")
