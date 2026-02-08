import os
from dotenv import load_dotenv
from prompt_templates import SUMMARY_PROMPT_TEMPLATE, EMAIL_REVISE_TEMPLATE
from openai_service import OpenAIService


# Load API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_client = OpenAIService(api_key=OPENAI_API_KEY)



if __name__ == "__main__":
    # print(f"Paste your text below to summarize:\n")
    print(f"Paste your text below to revise:\n")
    user_input = input()
    # prompt = SUMMARY_PROMPT_TEMPLATE.format(original_text=user_input)
    # summary = openai_client.generative_ai_with_prompt(prompt=prompt, role="summarizer")
    # print(f"\nSummary:\n{summary}")
    prompt = EMAIL_REVISE_TEMPLATE.format(original_text=user_input)
    summary = openai_client.generative_ai_with_prompt(prompt=prompt, role="email reviser")
    print(f"\nRevised Email:\n{summary}")