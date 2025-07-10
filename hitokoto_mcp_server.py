#!/usr/bin/env python3
"""Hitokoto tools for MCP Streamable HTTP server."""

import argparse
from hitokoto import load_hitokoto_items, read_hitokoto
import logging

import uvicorn
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server for Hitokoto tools.
# Setting json_response=True for better compatibility with MCP clients
# Setting stateless_http=True for better HTTP transport handling
mcp = FastMCP(name="hitokoto", json_response=True, stateless_http=True)


@mcp.tool()
async def get_hitokoto() -> str:
    """Get a random hitokoto (一言).

    Returns a random inspirational quote or sentence from the hitokoto collection.
    """
    try:
        logger.info("Getting hitokoto...")
        hitokoto = read_hitokoto()
        logger.info(f"Successfully got hitokoto: {hitokoto[:50]}...")
        return hitokoto
    except Exception as e:
        logger.error(f"Error getting hitokoto: {str(e)}")
        return f"Error getting hitokoto: {str(e)}"


if __name__ == "__main__":
    logger.info("Loading hitokoto items...")
    load_hitokoto_items()
    logger.info("Hitokoto items loaded successfully")

    parser = argparse.ArgumentParser(
        description="Run Hitokoto MCP Streamable HTTP server"
    )
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8124, help="Port to listen on")
    args = parser.parse_args()

    logger.info(f"Starting MCP server on {args.host}:{args.port}")
    uvicorn.run(
        mcp.streamable_http_app, host=args.host, port=args.port, log_level="info"
    )
