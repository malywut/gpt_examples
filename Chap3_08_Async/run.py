import asyncio
from openai import AsyncOpenAI
client = AsyncOpenAI()

async def async_call():
    response= await client.chat.completions.create(
    model="gpt-4",
    messages=[{
        "role": "user",
        "content": "Write a 10 lines story for my 5 year old."}]
    )
    print(response.choices[0].message.content)


asyncio.run(async_call())