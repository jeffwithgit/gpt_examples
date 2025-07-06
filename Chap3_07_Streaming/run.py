from openai import OpenAI
import httpx
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(http_client=httpx.Client())

stream = client.chat.completions.create(
model="gpt-4",
messages=[{
    "role": "user",
    "content": "Write a 10 lines story for my 5 year old."}],
stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
"""
output: (streaming output one by one)
Once upon a time, in a land where trees could talk, lived a little squirrel named Chip. Chip was small but bursting with energy and curiosity. One day, Chip heard a faint tune flowing through the forest. It was the Song Tree, singing the sweetest melody. Excited, Chip scampered up the tree to find the source of the music. 

He met a magic bird named Melody, who said, "Greetings little one, my songs can make wishes come true!". Badly wanting a fluffy tail like his friends, Chip wished for the fluffiest tail ever. Melody sang, and Chip’s tail poofed up! He rushed to the river to see his reflection, bursting with joy. From then onwards, he was the proudest and happiest squirrel in the forest with the fluffiest tail.
"""
