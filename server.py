# server.py
from fastmcp import FastMCP
from typing import Optional

# Initialize your MCP server
# The name will be used in Smithery
mcp = FastMCP(name="Simple Hello MCP")

@mcp.tool()
async def say_hello(name: str, formal: bool = False) -> str:
    """
    Greets a person.
    """
    if formal:
        return f"Greetings, {name}. It is an honor to make your acquaintance."
    else:
        return f"Hello, {name}! Nice to meet you."

# This block allows you to run the server locally for testing
if __name__ == "__main__":
    import uvicorn
    # When running remotely (e.g., on Smithery/Docker), the server will be
    # accessed via HTTP. FastMCP automatically configures for HTTP.
    # For local testing, you can use stdio or http as well.
    # Smithery deployments typically use Streamable HTTP.
    print("Running MCP server locally via HTTP on port 8000...")
    uvicorn.run(mcp.http_app, host="0.0.0.0", port=8000)