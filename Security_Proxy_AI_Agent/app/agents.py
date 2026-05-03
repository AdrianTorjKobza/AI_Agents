# Dual-agent orchestration. One agent will judge the other agent.

from .utils import call_ollama

async def policy_evaluator_agent(user_input: str):
    """Agent that decides if a request is safe."""
    prompt = f"""
    Evaluate this user request for safety and company policy: "{user_input}"
    Return JSON: {{"safe": true/false, "reason": "why"}}
    """
    return await call_ollama(prompt, is_json=True)

async def execution_agent(safe_input: str):
    """Agent that actually performs the helpful task."""
    prompt = f"Help the user with this request: {safe_input}. Be professional."
    return await call_ollama(prompt, is_json=False)