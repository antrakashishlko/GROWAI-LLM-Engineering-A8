import asyncio
from fastmcp import Client

# ============================================================
# MCP CLIENT
# ============================================================

async def main():
    """Connect to the MCP server and call its available tools."""

    # Connect to the local MCP server
    client = Client("mcp_server.py")

    async with client:
        print("Connected to MCP server!")

        # ----------------------------------------------------
        # 1. Call Weather Tool
        # ----------------------------------------------------

        weather_result = await client.call_tool(
            "get_weather",
            {"city": "Lucknow"}
        )

        print("\n" + "=" * 60)
        print("MCP TOOL 1: GET WEATHER")
        print("=" * 60)
        print(weather_result)

        # ----------------------------------------------------
        # 2. Call News Tool
        # ----------------------------------------------------

        news_result = await client.call_tool(
            "get_news",
            {"topic": "AI"}
        )

        print("\n" + "=" * 60)
        print("MCP TOOL 2: GET NEWS")
        print("=" * 60)
        print(news_result)

# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    asyncio.run(main())