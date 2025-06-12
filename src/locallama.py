from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


#Prompt template
prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer following questions"),
        ("user", "Context: {input}")
    ]
)

# Streamlit Framework
st.title("Chatbot with Langchain and Ollama")
input_text = st.text_input("Enter your question:")

# LLM
llm= Ollama(
    model= "deepseek-r1:8b"
)
output_parser= StrOutputParser()
#Chain
chain= prompt | llm | output_parser
if input_text:
    response= chain.invoke({"input": input_text})
    st.write("Response:", response)
    # Alternatively, you can use:
    # st.write(chain.invoke({"input": input_text}))
# Note: Make sure to have the Ollama server running and the model downloaded.
# You can run the Ollama server with the command:
# ollama serve --model deepseek-r1:8b
