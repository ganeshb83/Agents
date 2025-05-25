"""
Contextual Stock Analysis Agent

This module provides a persistent agent that maintains conversation history
and context across multiple interactions. It's ideal for:
- Multi-turn financial analysis
- Long-running investment discussions
- Context-aware recommendations
"""

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.storage.sqlite import SqliteStorage

# Load configuration
load_dotenv(override=True)

# Configure persistent storage for conversation history
storage = SqliteStorage(
    table_name="agent",
    db_file="tmp/agent.db",
    schema_version=1,
    auto_upgrade_schema=True,
    mode="agent"
)

# Initialize agent with context capabilities
agent_with_context = Agent(
    # Session identifiers
    user_id="U-123",
    session_id="S-123",

    # Model configuration
    model=Gemini(
        id=os.getenv("DEFAULT_MODEL"),
        vertexai=os.getenv("GOOGLE_GENAI_USE_VERTEXAI"),
        project_id=os.getenv("GOOGLE_CLOUD_PROJECT"),
        location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    ),

    # Core capabilities
    tools=[ReasoningTools(add_instructions=True)],
    add_history_to_messages=True,
    # Interaction guidelines
    instructions=[
        "Present data in clear tables",
        "Use available tools when needed",
        "Maintain conversation context"
    ],

    # System configuration
    monitoring=True,
    telemetry=True,
    storage=storage
)

# Demo: Context retention example
if __name__ == "__main__":
    print("\n=== Context Retention Demo ===")
    
    # First interaction
    agent_with_context.print_response("My name is Ganesh")
    
    # Second interaction - demonstrates context awareness
    agent_with_context.print_response("What is my name?")
