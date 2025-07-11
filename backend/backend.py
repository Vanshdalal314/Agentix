#Setup Pydantic model
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

#Setup AI Agent from frontend request
from fastapi import FastAPI

ALLOWED_MODEL_NAMES=["llama-3.3-70b-versatile", "llama3-70b-8192"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select valid AI model."}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    #Create AI Agent and get response from it!
    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)