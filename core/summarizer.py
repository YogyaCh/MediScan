import openai
from config.settings import OPENAI_API_KEY, DEFAULT_MODEL

openai.api_key = OPENAI_API_KEY

def generate_summary(report_text, knowledge):
    messages = [{
        "role": "user",
        "content": f"""You are a medical assistant. Use the lab report and knowledge below to summarize abnormalities.
        
        LAB REPORT:
        {report_text}

        KNOWLEDGE:
        {knowledge}

        SUMMARY:"""
            }]
    response = openai.chat.completions.create(model=DEFAULT_MODEL, messages=messages)
    return response.choices[0].message.content

def answer_question(report_text, question, knowledge):
    messages = [{
        "role": "user",
        "content": f"""Use this lab report and knowledge to answer:

        REPORT:
        {report_text}

        KNOWLEDGE:
        {knowledge}

        QUESTION: {question}
        ANSWER:"""
            }]
    response = openai.chat.completions.create(model=DEFAULT_MODEL, messages=messages)
    return response.choices[0].message.content
