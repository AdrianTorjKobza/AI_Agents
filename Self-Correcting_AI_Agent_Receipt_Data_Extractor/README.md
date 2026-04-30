# Self-Correcting Data Extractor AI Agent

A self-correcting AI Agent built with **FastAPI**, **Pydantic**, and **Ollama**. This project demonstrates an agentic workflow where an LLM extracts structured data from unstructured text and automatically corrects its own mistakes through a feedback loop.

## Features
- **Agentic Orchestration:** Implements a retry loop that uses validation errors to prompt the LLM for corrections.
- **Local-First:** Runs entirely offline using Ollama, ensuring data privacy and security.
- **Strict Validation:** Uses Pydantic models to guarantee 100% valid JSON output.
- **Async API:** Built with FastAPI for high-performance, non-blocking requests.

## Tech Stack
- **Language:** Python 3.10+
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **LLM Engine:** Ollama (running Llama 3.2)
- **Validation:** Pydantic

## How the Agentic Loop Works
- **Input:** User sends unstructured text (e.g. a receipt).
- **First Pass:** The system prompts the LLM to extract JSON.
- **Validation** Pydantic checks the JSON against a predefined schema.
- **Error Handling:** If validation fails (e.g., missing fields or wrong types), the error message is fed back into the LLM.
- **Success:** Once the data passes validation, the API returns the clean, structured response.

## Prerequisites
1. [Ollama](https://ollama.ai/) installed and running.
2. Pull the model: `ollama pull llama3.2`
3. Python 3.10 or higher.