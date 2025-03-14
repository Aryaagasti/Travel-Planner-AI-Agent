import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    SERPAPI_KEY = os.getenv('SERPAPI_KEY')
    GEMINI_KEY = os.getenv('GEMINI_KEY')
