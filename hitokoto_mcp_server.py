#!/usr/bin/env python3
"""Hitokoto tools for MCP Streamable HTTP server."""

import argparse
from hitokoto import load_hitokoto_items, read_hitokoto

import uvicorn
from mcp.server.fastmcp import FastMCP


# Initialize FastMCP server for Hitokoto tools.
# If json_response is set to True, the server will use JSON responses instead of SSE streams
# If stateless_http is set to True, the server uses true stateless mode (new transport per request)
mcp = FastMCP(name="hitokoto", json_response=False, stateless_http=False)


@mcp.tool()
async def get_hitokoto() -> str:
    """Get a random hitokoto (一言).
    
    Returns a random inspirational quote or sentence from the hitokoto collection.
    """
    try:
        hitokoto = read_hitokoto()
        return hitokoto
    except Exception as e:
        return f"Error getting hitokoto: {str(e)}"


if __name__ == "__main__":
    # Load hitokoto items at startup
    load_hitokoto_items()
    
    parser = argparse.ArgumentParser(description="Run Hitokoto MCP Streamable HTTP server")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8124, help="Port to listen on")
    args = parser.parse_args()

    # Start the server with Streamable HTTP transport
    uvicorn.run(mcp.streamable_http_app, host=args.host, port=args.port)
