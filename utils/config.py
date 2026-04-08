import os
from pathlib import Path

from dotenv import load_dotenv

_env_path = Path(__file__).with_name(".env")
load_dotenv(_env_path)

USAJOBS_API_KEY = os.getenv("USAJOBS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")