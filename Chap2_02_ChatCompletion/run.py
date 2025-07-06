from dotenv import load_dotenv
import httpx

load_dotenv()
from openai import OpenAI

client = OpenAI(http_client=httpx.Client())

# For GPT 3.5 Turbo, the endpoint is ChatCompletion
response = client.chat.completions.create(model="gpt-3.5-turbo",
# Conversation as a list of messages.
messages=[
    {"role": "system", "content": "You are a helpful teacher."},
    {
        "role": "user",
        "content": "Are there other measures than time complexity for an \
        algorithm?",
    },
    {
        "role": "assistant",
        "content": "Yes, there are other measures besides time complexity \
        for an algorithm, such as space complexity.",
    },
    {"role": "user", "content": "What is it?"},
])

print(response.choices[0].message.content)
"""
output:
Space complexity refers to the amount of memory space required by an algorithm to solve a problem as a function of the input size. It helps determine how much memory an algorithm needs to perform a task and is usually measured in terms of the amount of memory used in the worst-case scenario. Just like time complexity, space complexity can be expressed using Big O notation to describe the upper bound on the amount of memory used by an algorithm as the input size grows.
"""