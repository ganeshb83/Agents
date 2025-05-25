import os
from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools


# Load environment variables from .env file
load_dotenv(override=True)
print('model')
print(os.getenv("DEFAULT_MODEL"))
print(os.getenv("GOOGLE_GENAI_USE_VERTEXAI"))
print(os.getenv("GOOGLE_CLOUD_PROJECT"))
print(os.getenv("GOOGLE_CLOUD_LOCATION"))
#
agent = Agent(
    model=Gemini(
        id=os.getenv("DEFAULT_MODEL"),
        vertexai=os.getenv("GOOGLE_GENAI_USE_VERTEXAI"),
        project_id=os.getenv("GOOGLE_CLOUD_PROJECT"),
        location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    ),
    tools=[
        YFinanceTools(stock_price=True, stock_fundamentals=True, analyst_recommendations=True, company_info=True, historical_prices=True, company_news=True),
        ReasoningTools(add_instructions=True),
    ],
    instructions=[
        "Use tables to display data.",
        "Use the tools provided to get the data you need."
    ]
)


# agent.print_response(
#     "What are the stock prices of Commonwealth bank of Australia and Westpac banking corporation?",
#     stream=True)

agent.print_response(
    "Write a report on APPL and TSLA advise on the future of these stocks and what an investor should do in terms or buy or sell?",
    stream=True)