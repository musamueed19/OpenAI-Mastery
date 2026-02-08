import os
import streamlit as st
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

prompt_template = PromptTemplate(
    input_variables=["country", "language"],
    template=(
        """
        You are an expert in traditional cuisine.
        Provide a concise (2-4 sentence) explanation answering: What is the traditional cuisine of {country}?
        Respond in {language}.
        """
    ),
)

st.title("Traditional Cuisine Mini Project")
country = st.text_input("Enter a country to learn about its traditional cuisine:", placeholder="e.g. Pakistan")
language = st.text_input("Enter a language to get the response in that language", placeholder="Optional: Default English")

if not OPENAI_API_KEY:
    st.warning("OPENAI_API_KEY not set. Put your key in a .env file or export OPENAI_API_KEY.")

if OPENAI_API_KEY:
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY, n=1, max_tokens=500)
else:
    llm = None

if country:
    prompt_text = prompt_template.format(country=country, language=(language or "English"))
    if llm is None:
        st.error("OPENAI_API_KEY not set — cannot call the LLM. Set OPENAI_API_KEY and restart Streamlit.")
    else:
        # ChatOpenAI is not callable; use invoke(...) which returns an AIMessage
        try:
            ai_message = llm.invoke([
                ("system", "You are a helpful assistant that answers about traditional cuisines."),
                ("human", prompt_text),
            ])
            print(f"LLM returned: {ai_message}")
            # ai_message is an AIMessage; show the content
            content = getattr(ai_message, "content", None)
            if content is None:
                # Fallback: try string conversion
                content = str(ai_message)
            st.subheader(f"Traditional Cuisine of {country}:")
            st.write(content)
        except Exception as e:
            st.error(f"Error calling the LLM: {type(e).__name__}: {e}")