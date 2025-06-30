# server.py
from mcp.server.fastmcp import FastMCP

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
    mcp.run(transport="stdio")