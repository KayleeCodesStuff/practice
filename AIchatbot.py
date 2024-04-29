import asyncio

from g4f.client import AsyncClient
from g4f.Provider import BingCreateImages, OpenaiChat, Gemini

from g4f.client import Client

client = Client()

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Give me a compatibility ANALYSIS BETWEEN TAURUS AND A LIBRA"}],
)

print(chat_completion.choices[0].message.content or "")