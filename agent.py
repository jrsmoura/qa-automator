from google.adk.agent.agent import Agent
from prompt import ORCHETRATOR_PRMT


orchestrator_agent = Agent(
    name="Orchestrator Agent",
    role="An orchestrator that manages and delegates tasks to specialized agents based on the provided objectives.",
    prompt=ORCHETRATOR_PRMT,
)