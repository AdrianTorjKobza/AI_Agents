from fastmcp import FastMCP
from duckduckgo_search import DDGS

# Initialize the server
mcp = FastMCP("WebResearcher")

# --- TOOL 1: Web Search ---
@mcp.tool()
def search_web(query: str, max_results: int = 5) -> str:
    """
    Search the live web for a query. 
    Returns the title, URL, and a short snippet for the top 5 results.
    """
    try:
        with DDGS() as ddgs:
            # text() performs a standard web search.
            results = list(ddgs.text(query, max_results = max_results))
            
            if not results:
                return f"No web results found for: {query}"

            formatted_results = []

            for i, r in enumerate(results, 1):
                entry = (
                    f"{i}. {r['title']}\n"
                    f"   URL: {r['href']}\n"
                    f"   Snippet: {r['body']}\n"
                )
                formatted_results.append(entry)
            
            return "\n".join(formatted_results)
            
    except Exception as e:
        return f"Error connecting to the web: {str(e)}"

# --- TOOL 2: Quick Fact ---
@mcp.tool()
def get_instant_answer(query: str) -> str:
    """
    Get a direct, concise answer for facts, definitions, or calculations.
    """
    try:
        with DDGS() as ddgs:
            # answers() tries to find a 'Wikipedia-style' instant box.
            results = list(ddgs.answers(query))

            if results:
                return f"Answer: {results[0]['text']}\nSource: {results[0]['url']}"
            
            return "No instant answer available. Try using 'search_web' instead."
    
    except Exception:
        return "Could not retrieve an instant answer."

if __name__ == "__main__":
    mcp.run()