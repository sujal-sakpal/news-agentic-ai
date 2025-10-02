import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if "TAVILY_API_KEY" not in os.environ:
    raise ValueError("Tavily API key not found in environment variables. Please set TAVILY_API_KEY.")