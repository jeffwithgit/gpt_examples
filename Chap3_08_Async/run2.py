import asyncio
import time
from openai import AsyncOpenAI
from dotenv import load_dotenv
import httpx
load_dotenv()
client = AsyncOpenAI(http_client=httpx.AsyncClient())

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
"""
output:
Countdown: 10

Countdown: 9
Once upon a time, there was a little blue bird named Bella. She loved to sing songs every morning to start her day. The flowers would sway and the
Countdown: 8
 sun would shine brighter hearing Bella’s song. But one day, Bella lost her song and felt really sad. Yet, Bella didn't give up. She looked
Countdown: 7
 at the shining sun and tried again, but no song came out. Determined, Bella asked her friends, the squir
Countdown: 6
rels and the butterflies for help. They cheered for Bella, and to Bella's surprise, a beautiful tune filled the air. Bella realized that sometimes, we need a little help from
Countdown: 5
 friends, and from that day, her song sounded even sweeter than before. And every morning turned lovelier with Bella's song aided by her friends.
Countdown: 4

Countdown: 3

Countdown: 2

Countdown: 1
"""