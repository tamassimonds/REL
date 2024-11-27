import os

import aiohttp
import json

from typing import Optional, Dict, Any
from openai import AsyncOpenAI
import asyncio
import requests




# Load environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')  # Get from environment variable
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

#hf_client = InferenceClient(token=hf_api_token)  # Replace with your Hugging Face token

# Initialize clients
async_openai_client = AsyncOpenAI(api_key=openai_api_key)

# Add NVIDIA API key
async def generate_text(model: str, prompt: str, max_tokens: int = 16384, temperature: float = 0) -> str:
    """
    Asynchronously generate text using various AI models.
    
    :param model: The name of the model to use (e.g., "gpt-3.5-turbo", "claude-2", "meta-llama/Llama-2-70b-chat-hf")
    :param prompt: The input prompt for text generation
    :param max_tokens: Maximum number of tokens to generate
    :param temperature: Controls randomness in generation (0.0 to 1.0)
    :return: Generated text as a string
    """
    
    # OpenAI models
    
   
    
    if model.startswith("gpt-") or model.startswith("o1"):
        response = await async_openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content.strip()
    
    elif model.startswith("ft:gpt") or model.startswith("o1"):
        response = await async_openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content.strip()
    
   