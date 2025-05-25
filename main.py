"""
Stock Analysis Agent using Agno Framework

This script demonstrates a financial analysis agent that can:
- Fetch real-time stock data using YFinance
- Generate investment insights
- Maintain conversation context
- Use reasoning for complex analysis
"""

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools
from agno.storage.sqlite import SqliteStorage

# Load configuration from .env file
load_dotenv(override=True)

# Initialize the financial analysis agent
agent = Agent(
    # Configure Gemini model with environment variables
    model=Gemini(
        id=os.getenv("DEFAULT_MODEL"),
        vertexai=os.getenv("GOOGLE_GENAI_USE_VERTEXAI"),
        project_id=os.getenv("GOOGLE_CLOUD_PROJECT"),
        location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    ),
    # Configure data sources and tools
    tools=[
        YFinanceTools(
            stock_price=True,
            stock_fundamentals=True,
            analyst_recommendations=True,
            company_info=True,
            historical_prices=True,
            company_news=True
        ),
        ReasoningTools(add_instructions=True),
    ],
    # Agent behavior guidelines
    instructions=[
        "Present data in clear, structured tables",
        "Use available tools for accurate information"
    ]
)

# Example 1: Basic stock price query
print("\n=== Stock Price Check ===")
agent.print_response(
    "Show current stock prices for Commonwealth Bank of Australia and Westpac",
    stream=True
)

# Example 2: In-depth stock analysis
print("\n=== Stock Analysis Report ===")
agent.print_response(
    "Analyze AAPL and TSLA. Provide investment recommendations "
    "with buy/sell advice and future outlook.",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True
)
