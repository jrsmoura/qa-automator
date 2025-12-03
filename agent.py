from google.adk import Agent
from .prompt import ORCHESTRATOR_PRMT


root_agent = Agent(
    model = "gemini-2.5-flash",
    name="Orchestrator_Agent",
    description="An orchestrator that manages and delegates tasks to specialized agents based on the provided objectives.",
    instruction=ORCHESTRATOR_PRMT,
)