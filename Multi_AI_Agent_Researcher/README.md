# Multi-Agent Researcher

An event-driven backend that orchestrates multiple AI agents to perform research tasks asynchronously. This mimics a production-grade AWS environment using Step Functions and SQS.

## Tech Stack
- **Framework:** FastAPI (Asynchronous API)
- **AI Orchestration:** Multi-Agent Pipeline (Scout + Writer pattern)
- **Inference Engine:** Ollama (Local LLM)
- **Task Management:** BackgroundTasks (Simulating AWS SQS/Lambda)
- **Storage:** Local File System (Simulating Amazon S3)

## The Pipeline
1. **Submission:** User POSTs a topic. The API returns a `task_id` immediately.
2. **Scout Agent:** In the background, Agent 1 breaks the topic into research points.
3. **Writer Agent:** Agent 2 synthesizes the points into a professional summary.
4. **Persistence:** The final report is saved to the `/reports` directory.

## Setup
1. `pip install -r requirements.txt`
2. `ollama pull llama3.2`
3. `uvicorn app.main:app --reload`

## Testing
1. **Start Research:** 
   `POST /research?topic=The impact of 5G on IoT`
2. **Check Status:** 
   `GET /status/{task_id}`