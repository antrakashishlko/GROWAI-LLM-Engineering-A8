from fastmcp import FastMCP

# ============================================================
# 1. CREATE MCP SERVER
# ============================================================

mcp = FastMCP("Research MCP Server")

# ============================================================
# 2. WEATHER TOOL
# ============================================================

@mcp.tool
def get_weather(city: str) -> str:
    """Return mock weather information for a city."""

    weather_data = {
        "lucknow": "Lucknow: 32°C, partly cloudy.",
        "delhi": "Delhi: 35°C, sunny.",
        "mumbai": "Mumbai: 29°C, humid and cloudy.",
        "london": "London: 18°C, cloudy.",
        "new york": "New York: 24°C, partly cloudy."
    }

    return weather_data.get(
        city.lower(),
        f"No weather information available for {city}."
    )

# ============================================================
# 3. NEWS TOOL
# ============================================================

@mcp.tool
def get_news(topic: str) -> str:
    """Return mock news information about a topic."""

    news_data = {
        "ai": (
            "AI news: Researchers continue to develop "
            "more capable and efficient AI systems."
        ),
        "technology": (
            "Technology news: New AI and computing technologies "
            "are being developed rapidly."
        ),
        "science": (
            "Science news: Researchers are making progress "
            "in AI, space and biotechnology."
        )
    }

    return news_data.get(
        topic.lower(),
        f"No news information available for {topic}."
    )

# ============================================================
# 4. RUN MCP SERVER
# ============================================================

if __name__ == "__main__":
    print("MCP server starting...")
    mcp.run()
