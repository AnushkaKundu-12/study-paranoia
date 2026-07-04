from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

search_agent= Agent(
    name='search_agent',
    model='gemini-2.5-flash',
    instruction='you are a search agent of a personalised learning agent. Your work is use the google_search tool and search the web for real and relavant results,given a query ',
    tools=[google_search]
)    