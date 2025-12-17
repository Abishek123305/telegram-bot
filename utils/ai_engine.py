import openai
import config

openai.api_key = config.OPENAI_KEY

def ask_ai(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"]
