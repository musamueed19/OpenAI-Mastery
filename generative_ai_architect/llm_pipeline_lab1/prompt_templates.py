SUMMARY_PROMPT_TEMPLATE = """
You are a expert assistant for summarizing the content of a document.
Given the following below text, please provide a summary into 3 concise bullet points.
----
Text: {original_text}
----
Bullet Points;
"""
EMAIL_REVISE_TEMPLATE = """
Revise the following email to sound more professional,
but keep it short and polite:
---
Text: {original_text}
---
Rewritten Email:
"""