# test_client.py
import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport # Explicitly import for clarity

async def main():
    # Instantiate the client, pointing to your local server's URL.
    # The Client will automatically infer StreamableHttpTransport for HTTP URLs.
    # We also pass the URL with the trailing slash as we found it preferred.
    client = Client("http://localhost:8000/mcp/")

    async with client: # This context manager handles connection and session
        print("Client connected. Listing tools...")
        tools = await client.list_tools()
        print("\n--- Discovered Tools ---")
        for tool in tools:
            print(f"Name: {tool}")
            print("-" * 20)

        print("\n--- Invoking say_hello tool ---")
        # Example: Invoke the say_hello tool
        result_alice = await client.call_tool("say_hello", name="Alice", formal=False)
        print(f"Result (Alice): {result_alice}")

        result_bob = await client.call_tool("say_hello", name="Bob", formal=True)
        print(f"Result (Bob, formal): {result_bob}")

if __name__ == "__main__":
    asyncio.run(main())