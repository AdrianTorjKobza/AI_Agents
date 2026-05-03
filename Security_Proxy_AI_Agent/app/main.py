from fastapi import FastAPI, HTTPException
import logging
import os
from .security import redact_pii, check_permission
from .agents import policy_evaluator_agent, execution_agent

# Local Audit Logging (Mimics CloudWatch).
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename='logs/audit.log', level=logging.INFO)

app = FastAPI(title="Enterprise Secure Agentic Gateway")

@app.post("/chat")
async def secure_chat(user_input: str):
    # 1. Redact PII immediately (Security first!)
    clean_input = redact_pii(user_input)
    
    # 2. Policy Guardrail (Check permissions)
    if not check_permission(clean_input):
        logging.warning(f"BLOCKED: Unauthorized action attempted: {clean_input}")
        return {"error": "Action blocked by security policy.", "code": 403}

    # 3. Agentic Policy Evaluation
    evaluation = await policy_evaluator_agent(clean_input)
    
    if not evaluation.get("safe", False):
        logging.warning(f"BLOCKED by AI: {evaluation.get('reason')}")
        return {"error": "AI Guardrail violation", "reason": evaluation.get("reason")}

    # 4. Execution (Only if all checks pass)
    response = await execution_agent(clean_input)
    
    logging.info(f"SUCCESS: Processed request: {clean_input[:50]}...")
    return {"response": response, "pii_scrubbed": "[REDACTED_EMAIL]" in clean_input}