from openai import OpenAI

class OpenAIService:
    def __init__(self, api_key=openai_key):
        self.client = OpenAI(api_key=api_key)

    def translate_text(self, text, target_language):
        prompt = f"""
        Translate the below text paragraph to this target language: {target_language},
        text paragraph: {text}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            n=1,
        )
        print(response.choices[0].message.content.strip())
        return response.choices[0].message.content.strip()