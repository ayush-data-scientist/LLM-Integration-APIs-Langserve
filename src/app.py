from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
# Load environment variables from .env file

load_dotenv() #Load dotenv file



#Prompt template
prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer following questions"),
        ("user", "Context: {input}")
    ]
)

#Streamlit Framework
st.title("Chatbot with Langchain and OpenAI")
input_text= st.text_input("Enter your question:")

#LLM
llm= ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=1000,
    openai_api_key=os.getenv('Open_AI_API_Key')

)

output_parser= StrOutputParser()

chain= prompt | llm | output_parser
if input_text:
    response= chain.invoke({"input": input_text})
    st.write("Response:", response)
    # Alternatvely st.write(chain.invoke({input: input_text})