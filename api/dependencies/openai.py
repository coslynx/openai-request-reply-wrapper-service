from typing import Optional
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI  # Version: 0.27.2

load_dotenv()  # Load environment variables from .env

def get_openai_client() -> OpenAI:
    """
    Creates and returns an OpenAI client instance.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable not found.")
    return OpenAI(api_key=openai_api_key)