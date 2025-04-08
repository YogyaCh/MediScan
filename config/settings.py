import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = "gpt-3.5-turbo"
RATE_LIMIT_CALLS_PER_MIN = 60
REFERENCE_PATH = "reference_knowledge"
TESSERACT_PATH = "/Users/yogyach/anaconda3/envs/mediscan/bin/tesseract"