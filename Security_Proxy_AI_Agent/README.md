# Enterprise Secure Agentic Gateway
A local implementation of a secure AI backend designed for enterprise compliance. This project mimics **AWS CloudWatch, Amazon Comprehend, and AWS IAM** patterns using Python and Ollama.

## Tech Stack
- **API Framework:** FastAPI
- **Security Layer:** Regex-based PII Redaction & Manual Policy Enforcement
- **Orchestration:** Dual-Agent Pattern (Evaluator + Executor)
- **Observability:** Local File Logging (Audit Trails)
- **Inference Engine:** Ollama

## Security Features
- **Data Masking:** Automatically redacts emails before they reach the LLM.
- **Action Guardrails:** Prevents destructive actions (delete/wipe) via a permission layer.
- **AI Governance:** A dedicated "Policy Agent" evaluates intent before the "Execution Agent" generates a response.

## Setup
1. `pip install -r requirements.txt`
2. `ollama pull llama3.2`
3. `uvicorn app.main:app --reload`

## Testing
1. **Test PII Redaction:** Send a message containing an email. Observe the audit logs.
2. **Test Blocked Action:** Try to ask the agent to "Delete all records."
3. **Test Safety:** Ask the agent to generate something harmful.