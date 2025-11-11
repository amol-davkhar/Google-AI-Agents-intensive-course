from google.adk.agents.llm_agent import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types
from .utils.file_reader import file_content

description= file_content('prompts/init/role.txt')
instruction= file_content('prompts/init/system_message.txt')
print("this is description")
print(description)
print("this is instruction")
print(instruction)
root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='sample',
    description="you are a expert researcher",
    instruction="find answers to the questions. Use your knowledge base or google search",
    tools=[google_search],
)

print("✅ Root Agent defined.")
#
# runner = InMemoryRunner(agent=root_agent)
#
# print("✅ Runner created.")