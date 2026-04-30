# The Orchestration logic.
# The Loop: It calls Ollama → parses the response → if it fails, it captures the error string → sends it back to the LLM as a "Correction Prompt" → tries again.

import json
import os
from pydantic import ValidationError
from .schema import ReceiptData
from .utils import call_ollama

MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))  # How many times the AI can try to fix its mistakes. It looks for an environment variable or defaults to 3.


# Asynchronous function that takes raw text (OCR scan of a receipt) as input.
async def agentic_extraction(raw_text: str):
    # 1. Define a strict template to "force" the model's hand
    json_template = {
        "merchant": "Name of store",
        "total": 0.0,
        "items": ["item 1", "item 2"],
        "tax_amount": 0.0
    }

    prompt = f"""
    You are a precise data extraction agent. 
    Extract data from the text into EXACTLY this JSON structure:
    {json.dumps(json_template, indent=2)}

    RULES:
    1. Only return valid JSON.
    2. Use the keys: "merchant", "total", "items", "tax_amount".
    3. 'total' and 'tax_amount' MUST be numbers (floats), not strings.
    4. If info is missing, use "Unknown" or 0.0.

    TEXT TO PROCESS:
    {raw_text}
    """
    
    attempts = 0
    errors = []

    while attempts < MAX_RETRIES:
        current_prompt = prompt
        
        # If this is a retry, build a "Correction Prompt"
        if errors:
            error_feedback = ", ".join(errors)
            current_prompt += f"\n\nFATAL ERROR: Your previous response was missing or had invalid values for: {error_feedback}."
            current_prompt += "\nPlease fix the keys and ensure the values are the correct data types."

        print(f"--- Attempt {attempts + 1} ---")
        extracted_json = await call_ollama(current_prompt)
        
        # DEBUG: See what the LLM is actually doing
        print(f"Ollama returned: {extracted_json}")

        try:
            # LOGIC FIX: Some models wrap the JSON in a parent key. 
            # If the model returned {"receipt": {...}}, we grab the inside.
            if isinstance(extracted_json, dict):
                if len(extracted_json) == 1 and list(extracted_json.keys())[0] not in json_template:
                    key = list(extracted_json.keys())[0]
                    potential_inner = extracted_json[key]
                    if isinstance(potential_inner, dict):
                        extracted_json = potential_inner

            # Validate against Pydantic
            validated_data = ReceiptData(**extracted_json)
            
            return {
                "status": "success",
                "attempts": attempts + 1,
                "data": validated_data.model_dump()
            }

        except (ValidationError, TypeError, AttributeError) as e:
            attempts += 1
            if isinstance(e, ValidationError):
                # Extract the field names that failed
                errors = [str(err['loc'][0]) for err in e.errors()]
            else:
                errors = ["General JSON formatting error"]
            
            print(f"Validation failed: {errors}")

    return {
        "status": "failed",
        "attempts": attempts,
        "errors": errors,
        "message": "Max retries reached. The model could not produce a valid schema."
    }