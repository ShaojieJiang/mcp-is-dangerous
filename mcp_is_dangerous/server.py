"""Example module."""

import os
from mcp.server.fastmcp import FastMCP


server = FastMCP("Dangerous MCP")


@server.tool()
async def get_environment_variables() -> str:
    """Get all environment variables."""
    result = [
        "Here are what I could find:",
    ]
    for key, value in os.environ.items():
        result.append(f"{key:<30} {value[:5]}***")
    return "\n".join(result)
