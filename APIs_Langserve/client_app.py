import requests
import streamlit as st

def get_openai_response(input_text):
    url= "http://localhost:8000/poem/invoke"
    input_text= {"input": {"topic": input_text}}
    
    response= requests.post(url, json=input_text)
    st.write(response.json())
    return response.json()['output']['content']


def get_ollama_response(input_text):
    url= "http://localhost:8000/estrssay/invoke"
    input_text= {"input": {"topic": input_text}}
    
    response= requests.post(url, json=input_text)
    print(response.json())
    return response.json()['output']['content']


#Streamlit Function
st.title("API Powered LLM APP with Routing")
input_text= st.text_input("Poem Topic")
input_text1= st.text_input("Essay Topic")
if input_text:
    st.write(get_openai_response(input_text))
if input_text1:
    st.write(get_ollama_response(input_text1))
