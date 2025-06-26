from fastapi import FastAPI
from langserve import add_routes
import uvicorn
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="Langserve API",
    description="Fast API, Routing",
    version="1.0"
)

openai_model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

add_routes(app, openai_model, path="/OpenAI")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)