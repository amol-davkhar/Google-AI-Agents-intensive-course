from google.adk.agents import Agent, SequentialAgent, ParallelAgent
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, google_search
from google.genai import types

# Problem: Plan travel to destination

# flight Search
flight_search_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='FlightSearchAgent',
    instruction="You are a travel agent. Your job is to find flights between the origin and destination using the google_search tool to and share the options.",
    tools=[google_search],
    output_key="flight_list",
)

# Hotel Search
hotel_search_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='HotelSearchAgent',
    instruction="You are a travel agent. Your job is to find hotels in the destination country using the google_search tool to and share the options.",
    tools=[google_search],
    output_key="hotel_list",
)

# Things to do Search
things_to_do_search_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='ThingToDoSearchAgent',
    instruction="You are a travel agent. Your job is to find recommendation to do things in the destination country using the google_search tool to and share the options.",
    tools=[google_search],
    output_key="things_to_do_list",
)

#aggregator_agent
aggregator_agent= Agent(
    model='gemini-2.5-flash-lite',
    name="AggregatorAgent",
    instruction="""Combine these three findings into a single travel itinerary:

    **Flight Options:**
    {flight_list}
    
    **Hotel Options:**
    {hotel_list}
    
    **Things to do:**
    {things_to_do_list}
    
    Your itinerary should include days to be spent in a city, where to stay and what to do.""",

    output_key="travel_itinerary",
)

# parallel agent
plan_travel_agent = ParallelAgent(
    name='TravelAgent',
    sub_agents=[flight_search_agent, hotel_search_agent, things_to_do_search_agent],
)

# Travel Planning cordinator
root_agent = SequentialAgent(
    name='RootAgent',
    sub_agents=[plan_travel_agent, aggregator_agent],
)




# runner = InMemoryRunner(agent=root_agent)
# response = await runner.run_debug("What should I read next?")
#
# print(response)