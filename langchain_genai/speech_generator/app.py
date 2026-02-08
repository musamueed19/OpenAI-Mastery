import os
from dotenv import load_dotenv

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


from prompts import CREATE_SPEECH_FROM_TITLE_PROMPT, CREATE_SPEECH_TITLE_PROMPT

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.title("Speech Generator")
topic = st.text_input("Enter a topic to generate a speech title and speech:", placeholder="e.g. The importance of education")

title_prompt = PromptTemplate(
    input_variables=["topic"],
    template=CREATE_SPEECH_TITLE_PROMPT,
)

speech_prompt = PromptTemplate(
    input_variables=["title"],
    template=CREATE_SPEECH_FROM_TITLE_PROMPT,
)

gpt_three_turbo = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY, n=1, max_tokens=700)
gpt_three_sub_version_turbo = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=OPENAI_API_KEY, n=1, max_tokens=700)
topic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that generates speech titles and speeches based on a given topic."),
    ("human", title_prompt.template),
])

eassy_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that generates speeches based on a given title."),
    ("human", speech_prompt.template),
])

title_chain = topic_prompt | gpt_three_turbo
eassy_chain = eassy_prompt | gpt_three_sub_version_turbo
final_chain = title_chain | StrOutputParser() | (lambda title: (st.subheader(f"Speech Title: {title}"), title)[1]) | eassy_chain

if topic:
    try:
        speech = final_chain.invoke({
            "topic": topic,
        })
        st.write(speech.content)
    except Exception as e:
        st.error(f"Error calling the LLM: {type(e).__name__}: {e}")