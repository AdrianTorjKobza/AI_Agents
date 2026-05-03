import httpx
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2")

async def call_ollama(prompt: str, is_json=True):
    """
    Service layer to communicate with Ollama.
    Handles both structured JSON and free-form text.
    """
    url = f"{OLLAMA_URL}/api/generate"
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    if is_json:
        payload["format"] = "json"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, timeout=60.0)
            response.raise_for_status()
            raw_content = response.json().get("response", "")

            if is_json:
                # Clean markdown if present
                clean_content = re.sub(r'```json\s*|```', '', raw_content).strip()
                return json.loads(clean_content)
            
            return raw_content.strip()
            
        except Exception as e:
            print(f"Ollama Error: {e}")
            return {"safe": False, "reason": "Error connecting to AI engine"} if is_json else "Service unavailable"