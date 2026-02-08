import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


prompt_template = PromptTemplate(
    input_variables=["country"],
    template="""
    You are an expert in traditional cuisine.
    You provide information about specific dish from a specific country.
    Answer the question: What is the traditional cuisine of {country}?
    """
)

st.title("Traditional Cuisine Mini Project")
country = st.text_input("Enter a country to learn about its traditional cuisine:")

if country:
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY, n=1, max_tokens=500)
    prompt = prompt_template.format(country=country)
    response = llm(prompt)
    st.subheader(f"Traditional Cuisine of {country}:")
    st.write(response)