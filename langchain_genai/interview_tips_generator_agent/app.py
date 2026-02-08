import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt_template = PromptTemplate(
    input_variables=["city", "month", "language"],
    template=(
        """
        Welcome to the city {city} travel guide!
        If you are visiting this city {city} in {month}, here are some tips and recommendations.
        1. Must-visit attractions in {city} during {month}.
        2. Local events or festivals happening in {city} in {month}.
        3. Weather conditions to expect in {city} during {month}.
        4. Recommended local cuisine or dishes to try in {city} during {month}.
        5. Useful phrases in the local language for travelers visiting {city} in {month}.
        Enjoy your trip!
        
        Respond in {language}.
        """
    ),
)

st.title("City Travel Guide")
city = st.text_input("Enter a city to get travel tips:", placeholder="e.g. Dubai")
month = st.text_input("Enter the month of your visit:", placeholder="e.g. July")
language = st.text_input("Enter a language to get the response in that language", placeholder="Default English")

if not OPENAI_API_KEY:
    st.warning("OPENAI_API_KEY not set. Put your key in a .env file or export OPENAI_API_KEY.")

if OPENAI_API_KEY:
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY, n=1, max_tokens=500)
else:
    llm = None

if city and month:
    prompt_text = prompt_template.format(city=city, month=month, language=(language or "English"))
    if llm is None:
        st.error("OPENAI_API_KEY not set — cannot call the LLM. Set OPENAI_API_KEY and restart Streamlit.")
    else:
        # ChatOpenAI is not callable; use invoke(...) which returns an AIMessage
        try:
            ai_message = llm.invoke([
                ("system", "You are an expert assistant that provides travel tips and recommendations."),
                ("human", prompt_text),
            ])
            print(f"LLM returned: {ai_message}")
            # ai_message is an AIMessage; show the content
            content = getattr(ai_message, "content", None)
            if content is None:
                # Fallback: try string conversion
                content = str(ai_message)
            st.subheader(f"Travel Guide for {city} in {month}:")
            st.write(content)
        except Exception as e:
            st.error(f"Error calling the LLM: {type(e).__name__}: {e}")