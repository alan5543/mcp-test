# Use a slim Python image as the base
FROM python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Ensure Python output is unbuffered
ENV PYTHONUNBUFFERED=1

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code into the container
COPY . .

# Expose the port your server will listen on. Smithery will use the PORT env var.
# We set a default of 8000, but Smithery will override it with its own assigned PORT.
ENV PORT=8000
EXPOSE $PORT

# Command to run your FastMCP server using uvicorn.
# `server:mcp.sse_app` means run the `sse_app` object from the `mcp` instance
# in `server.py`. FastMCP's `sse_app` is its Streamable HTTP application.
CMD ["uvicorn", "server:mcp.http_app", "--host", "0.0.0.0", "--port", "8000", "--factory"]
