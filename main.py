import os
from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.google import Gemini

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
   )
)


agent.print_response("What is the stock price of Commonwealth bank of Australia?", stream=True)