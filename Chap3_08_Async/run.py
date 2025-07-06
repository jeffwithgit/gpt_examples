import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
import httpx
load_dotenv()
client = AsyncOpenAI(http_client=httpx.AsyncClient())

async def async_call():
    response= await client.chat.completions.create(
    model="gpt-4",
    messages=[{
        "role": "user",
        "content": "Write a 10 lines story for my 5 year old."}]
    )
    print(response.choices[0].message.content)


asyncio.run(async_call())
"""
output:
Once upon a time in a jungle filled with colorful blossoms, there was a tiny, curious elephant named Elly. Elly was different because she had rainbow colored tusks. Everyone in the jungle admired her unique beauty. One day, her tusks lost their colors. Worried, Elly visited Wise Turtle, known for his ancient wisdom. Wise Turtle told her that her colors were not gone, but transferred to the flowers around. He taught her that sharing can sometimes mean losing something but adding beauty elsewhere. Happy with her discovery, Elly danced around the colorful blossoms, feeling more special than ever before. And from that day, the jungle sparkled with more colors thanks to Elly's rainbow tusks.
"""