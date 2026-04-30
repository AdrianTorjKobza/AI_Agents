# Synchronous Python function designed to communicate with the Ollama local server.

import httpx
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

async def call_ollama(prompt: str):
    # Reverting to /api/generate as your Ollama version requires it
    url = f"{OLLAMA_URL}/api/generate"
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "format": "json"  # Instructs Ollama's backend to facilitate JSON
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, timeout=60.0)
            
            if response.status_code != 200:
                raise Exception(f"Ollama returned {response.status_code}: {response.text}")

            # The /api/generate response structure is different from /api/chat
            # It returns the text directly in the 'response' key
            raw_content = response.json().get("response", "")
            
            # SANITIZE: Remove Markdown and extra whitespace
            clean_content = re.sub(r'```json\s*|```', '', raw_content).strip()
            
            if not clean_content:
                return {}

            return json.loads(clean_content)
            
        except json.JSONDecodeError:
            print(f"FAILED TO PARSE JSON: {raw_content}")
            return {}
        except Exception as e:
            raise Exception(f"Ollama connection error: {str(e)}")