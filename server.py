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
    print("Running MCP server locally via HTTP on port 8000...")
    # Use mcp.http_app and the --factory flag explicitly
    uvicorn.run("server:mcp.http_app", host="0.0.0.0", port=8000, factory=True)
    # Note: Changed to string "server:mcp.http_app" and added factory=True