
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display

import sys
print(sys.executable)

load_dotenv(override=True)
# openai_api_key = os.getenv('OPENAI_API_KEY')
# anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
# deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
# grok_api_key = os.getenv('GROK_API_KEY')
# openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# if openai_api_key:
#     print(f"[OK] OpenAI API Key exists and begins {openai_api_key[:8]}")
# else:
#     print("OpenAI API Key not set")
    
# if anthropic_api_key:
#     print(f"[OK] Anthropic API Key exists and begins {anthropic_api_key[:7]}")
# else:
#     print("Anthropic API Key not set (and this is optional)")

if google_api_key:
    print(f"[OK] Google API Key exists and begins {google_api_key[:2]}")
# else:
#     print("Google API Key not set (and this is optional)")

# if deepseek_api_key:
#     print(f"[OK] DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
# else:
#     print("DeepSeek API Key not set (and this is optional)")

if groq_api_key:
    print(f"[OK] Groq API Key exists and begins {groq_api_key[:4]}")
# else:
#     print("Groq API Key not set (and this is optional)")

# if grok_api_key:
#     print(f"[OK] Grok API Key exists and begins {grok_api_key[:4]}")
# else:
#     print("Grok API Key not set (and this is optional)")

# if openrouter_api_key:
#     print(f"[OK] OpenRouter API Key exists and begins {openrouter_api_key[:3]}")
# else:
#     print("OpenRouter API Key not set (and this is optional)")


# Connect to OpenAI client library
# A thin wrapper around calls to HTTP endpoints

# openai = OpenAI()
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

# For Gemini, DeepSeek and Groq, we can use the OpenAI python client
# Because Google and DeepSeek have endpoints compatible with OpenAI
# And OpenAI allows you to change the base_url

# anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
# deepseek_url = "https://api.deepseek.com"
groq_url = "https://api.groq.com/openai/v1"
grok_url = "https://api.x.ai/v1"
openrouter_url = "https://openrouter.ai/api/v1"
ollama_url = "http://localhost:11434/v1"

# anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)
# deepseek = OpenAI(api_key=deepseek_api_key, base_url=deepseek_url)
groq = OpenAI(api_key=groq_api_key, base_url=groq_url)
# grok = OpenAI(api_key=grok_api_key, base_url=grok_url)
# openrouter = OpenAI(base_url=openrouter_url, api_key=openrouter_api_key)
ollama = OpenAI(api_key="ollama", base_url=ollama_url)
