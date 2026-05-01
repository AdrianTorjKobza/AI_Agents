# Scout (Planning) and Writer (Synthesis) agents.

from .utils import call_ollama

async def scout_agent(topic: str):
    """Breaks a broad topic into specific research angles."""
    prompt = f"Topic: {topic}. Generate 3 specific research sub-points as a JSON list of strings called 'points'."
    result = await call_ollama(prompt)
    return result.get("points", [topic])

async def writer_agent(topic: str, research_data: list):
    """Synthesizes research points into a professional brief."""
    data_str = ", ".join(research_data)
    prompt = f"Topic: {topic}. Facts: {data_str}. Write a professional 2-paragraph research brief. Return as plain text."
    return await call_ollama(prompt, is_json=False)