from fastapi import FastAPI
from langserve import add_routes
import uvicorn

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="Langserve API",
    description="Fast API, Routing",
    version="1.0"
)

openai_model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
llama_model = Ollama(model="llama2:7b-chat")

prompt1 = ChatPromptTemplate.from_messages([
    ("system", "Write me an essay about {topic} with 100 words")
])
prompt2 = ChatPromptTemplate.from_messages([
    ("system", "Write me a poem about {topic} for a 5 year old child with 100 words")
])

add_routes(app, prompt1 | llama_model, path="/Essay")
add_routes(app, prompt2 | openai_model, path="/Poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)