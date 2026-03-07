# Usage example for the use_models_v1 module, which provides a unified interface to multiple LLM providers (Gemini, Groq, Ollama).
# ----------------------------------------------------
# import use_models_v1
# groq=use_models_v1.groq
# ----------------------------------------------------
# Gemini
# ======================
# gemini-2.5-flash-lite
# gemini-3-flash-preview
# 
# groq
# ======================
# llama-3.1-8b-instant
# llama-3.3-70b-versatile
# openai/gpt-oss-20b
# openai/gpt-oss-120b
# groq/compound

import os
# import requests
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display

import sys
print(sys.executable)

load_dotenv(override=True)

google_api_key = os.getenv('GOOGLE_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

# openai = OpenAI()
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GRPQ_BASE_URL = "https://api.groq.com/openai/v1"
OLLAMA_BASE_URL = "http://localhost:11434/v1"

gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
groq = OpenAI(base_url=GRPQ_BASE_URL,api_key=groq_api_key)
ollama = OpenAI(base_url=OLLAMA_BASE_URL,api_key="ollama")

def get_openai(model_name):
    if model_name.startswith("gemini"):
        return gemini
    elif model_name.startswith("groq"):
        return groq
    elif model_name.startswith("ollama"):
        return ollama
    else:
        raise ValueError(f"Unknown model name: {model_name}")
