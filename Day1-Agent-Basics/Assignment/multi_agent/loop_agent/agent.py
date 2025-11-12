from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, google_search, FunctionTool
from google.genai import types


def exit_loop():
    """Call this function ONLY when the critique is 'APPROVED', indicating the story is finished and no more changes are needed."""
    return {"status": "approved", "message": "critique has approved. Exiting refinement loop."}

# Problem: Create Contract for the asked usecase

# flight Search
initial_contract_creator = Agent(
    model='gemini-2.5-flash-lite',
    name='initialContractCreatorAgent',
    instruction="You are a legal advisor. Your job is to create a concise contract for the given user query.",
    tools=[google_search],
    output_key="current_contract",
)

# Hotel Search
critique_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='CriqueAgent',
    instruction="""You are a legal contract critic. Review the contract provided below.
    Contract: {current_contract}
    
    Evaluate the contract details and language.
    - If the contract is well-written and complete, you MUST respond with the exact phrase: "APPROVED"
    - Otherwise, provide 2-3 specific, actionable suggestions for improvement.""",
    tools=[google_search],
    output_key="critique",
)

# refiner
refiner_agent = Agent(
    name="RefinerAgent",
    model="gemini-2.5-flash-lite",
    instruction="""You are a contract refiner. You have a contract draft and critique.

    Contract Draft: {current_contract}
    Critique: {critique}

    Your task is to analyze the critique.
    - IF the critique is EXACTLY "APPROVED", you MUST call the `exit_loop` function and nothing else.
    - OTHERWISE, rewrite the contract draft to fully incorporate the feedback from the critique.""",

    output_key="current_contract",  # It overwrites the story with the new, refined version.
    tools=[FunctionTool(exit_loop)],  # The tool is now correctly initialized with the function reference.
)

# The LoopAgent contains the agents that will run repeatedly: Critic -> Refiner.
contract_refinement_loop = LoopAgent(
    name="ContractRefinementLoop",
    sub_agents=[critique_agent, refiner_agent],
    max_iterations=2, # Prevents infinite loops
)

# The root agent is a SequentialAgent that defines the overall workflow: Initial Write -> Refinement Loop.
root_agent = SequentialAgent(
    name="ContractPipeline",
    sub_agents=[initial_contract_creator, contract_refinement_loop],
)


# runner = InMemoryRunner(agent=root_agent)
# response = await runner.run_debug("What should I read next?")
#
# print(response)