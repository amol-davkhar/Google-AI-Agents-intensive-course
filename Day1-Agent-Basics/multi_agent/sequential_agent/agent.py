from google.adk.agents import Agent, SequentialAgent
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, google_search
from google.genai import types



# Problem: Give the 2025 most popular books in fiction in name, author, synopsis and rating format.

# Search for Books
search_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='SearchAgent',
    instruction="You are an expert book recommender. Your job is to find the top 10 2025 fiction hits using google_search tool to and present the findings with citations.",
    tools=[google_search],
    output_key="books_list",
)

# Output Formater
output_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='OutputAgent',
    instruction="Read the provided list of books : {books_list}. Provide output in format: [{name: book_n_name, author: book_n_author, synopsis: book_n_synopsis, rating: book_n_rating} ]",
    output_key="final_books_list",
)

# Execute these agents sequentially
root_agent = SequentialAgent(
    name='BookSearchAgent',
    sub_agents=[search_agent, output_agent],
)

# runner = InMemoryRunner(agent=root_agent)
# response = await runner.run_debug("What should I read next?")
#
# print(response)