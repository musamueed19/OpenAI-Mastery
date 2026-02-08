from openai import OpenAI

class OpenAIService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)
        
    def generative_ai_with_prompt(self, prompt, role="assistant"):
        """Create a chat completion using the OpenAI API."""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a powerful helpful {role}"
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            n=1,
            max_tokens=400,
        )
        return response.choices[0].message.content.strip()