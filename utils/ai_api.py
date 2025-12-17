# utils/ai_api.py

from groq import Groq
import config

client = Groq(api_key=config.GROQ_API_KEY)

def ask_ai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ FIXED MODEL
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant for students. Answer clearly and concisely."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=512
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ AI service error: {str(e)}"
