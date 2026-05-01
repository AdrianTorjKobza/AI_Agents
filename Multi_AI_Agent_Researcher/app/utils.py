# Ollama connection.

import httpx
import os
import json
from dotenv import load_dotenv

load_dotenv()

async def call_ollama(prompt: str, is_json=True):
    url = f"{os.getenv('OLLAMA_BASE_URL')}/api/generate"
    payload = {
        "model": os.getenv("MODEL_NAME"),
        "prompt": prompt,
        "stream": False
    }
    if is_json:
        payload["format"] = "json"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, timeout=90.0)
        res_json = response.json()
        content = res_json.get("response", "")
        return json.loads(content) if is_json else content