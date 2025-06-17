import os
from dotenv import load_dotenv

#Settingup API Keys
load_dotenv()
#GROQ API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ['GROQ_API_KEY'] = GROQ_API_KEY

#TAVILY API Key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY

#Model Setup
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
#Setup AI Agent
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    llm=ChatGroq(model=llm_id)

    tools=[TavilySearch(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt
    )

    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_message=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_message[-1]

