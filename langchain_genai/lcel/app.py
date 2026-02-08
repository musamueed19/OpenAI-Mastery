import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt_template = PromptTemplate(
    input_variables=["city", "month", "language"],
    template=(
        """
        You are an expert travel guide. For the city {city} and the month {month},
        produce a concise, practical numbered list of 5–7 travel tips that a visitor
        should know (attractions, events, weather, safety, cuisine, useful phrases).
        Do not include greetings or acknowledgements — only the numbered tips.

        City: {city}
        Month: {month}

        Provide the response in {language}.
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
    if llm is None:
        st.error("OPENAI_API_KEY not set — cannot call the LLM. Set OPENAI_API_KEY and restart Streamlit.")
    else:
        # create a chat prompt that embeds the system instruction and the human prompt template
        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert travel guide who gives concise, practical tips and no greetings."),
            ("human", prompt_template.template)   # prompt_template is your PromptTemplate instance
        ])
        # chain
        chain = chat_prompt | llm
        try:
            ai_message = chain.invoke({
                "city": city,
                "month": month,
                "language": (language or "English"),
            })
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