# MediScan AI – Medical Lab Report Analyzer

MediScan is a lightweight GenAI-powered tool that processes unstructured medical lab reports in PDF format, extracts key biomarkers using OCR and LLMs, and enables users to ask questions about the report — all through a clean, interactive web UI.
You can check it out on: https://cliniq.streamlit.app

---

## Project Goal

Manual extraction and interpretation of lab values from medical reports is time-consuming and error-prone. MediScan addresses this by:
- Automatically extracting test names, values, and units from PDF-based lab reports.
- Generating a structured summary from unstructured OCR text.
- Allowing users to ask questions like:  
  *"Is the blood glucose level normal?"*  
  *"What are the abnormal values in this report?"*

This project was independently developed in under 48 hours to showcase applied GenAI skills in a real-world context.

---

## Tech Stack

| Layer        | Tool/Library         | Purpose                         |
|--------------|----------------------|----------------------------------|
| LLM          | OpenAI GPT-3.5 Turbo | Lab value extraction, Q&A       |
| OCR          | Tesseract OCR / PaddleOCR | Extract text from scanned PDFs |
| PDF Handling | pdf2image            | Convert PDF pages to images     |
| UI           | Streamlit            | Interactive web interface       |
| Backend      | Python               | Core logic and API integrations |
| Hosting      | Streamlit Cloud      | 1-click cloud deployment        |

---

## Sample UI

![MediScan Screenshot](https://placehold.co/600x300?text=Demo+Screenshot)

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yogyach/mediscan-ai.git
cd mediscan-ai
```
### 2. Create and Activate the Conda Environment
```bash
conda env create -f environment.yml
conda activate mediscan
```

### 3. Install Tesseract OCR
```bash
conda install -c conda-forge tesseract
which tesseract
# Should return something like: /Users/yourname/anaconda3/envs/mediscan/bin/tesseract
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

### 5. Create and Add Your OpenAI API Key

#### 1. Go to: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)  
#### 2. Click **“Create new secret key”**  
#### 3. Copy it, then create a `.env` file:

```bash
touch .env
```

Paste this inside `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
