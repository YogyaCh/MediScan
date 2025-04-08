import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(report_text: str, knowledge: str) -> str:
    prompt = f"""
    You are a medical assistant. Use the following lab report and clinical knowledge to generate a summary. 
    Focus on identifying abnormal values and briefly explaining what they might indicate.

    LAB REPORT:
    {report_text}

    CLINICAL KNOWLEDGE:
    {knowledge}

    SUMMARY:
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message["content"]

def answer_question(report_text: str, user_question: str, knowledge: str) -> str:
    prompt = f"""
    You are a helpful AI assistant. Use the lab report and clinical knowledge below to answer the user's question.

    LAB REPORT:
    {report_text}

    CLINICAL KNOWLEDGE:
    {knowledge}

    QUESTION: {user_question}
    ANSWER:
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=300
    )
    return response.choices[0].message["content"]

