from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .agent import agentic_extraction

app = FastAPI(title="Agentic Receipt Extractor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],
)

class ExtractionRequest(BaseModel):
    text: str # Define what a valid request looks like.

# Check if the server is running.
@app.get("/health")
def health_check():
    return {"status": "online"}

# We use POST because we are sending data (the receipt text) to the Ollama server.
@app.post("/extract")
async def extract_data(request: ExtractionRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Text input cannot be empty")
        
        result = await agentic_extraction(request.text)
        return result
    except Exception as e:
        # This will return the ACTUAL error to your Swagger UI/Postman
        return {"debug_error": str(e), "type": str(type(e))}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # Starts Uvicorn, the lightning-fast web server that actually "hosts" the FastAPI code on port 8000.