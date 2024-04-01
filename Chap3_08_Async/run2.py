import asyncio
import time
from openai import AsyncOpenAI
client = AsyncOpenAI()

async def async_call():
    stream =  await client.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "user",
            "content": "Write a 10 lines story for my 5 year old."}],
        stream=True
    )

    async for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

async def countdown():
    for i in range(10, 0, -1):
        print(f"\nCountdown: {i}")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(async_call(), countdown())

asyncio.run(main())