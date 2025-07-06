from openai import OpenAI
import httpx
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(http_client=httpx.Client())

# Call the openai ChatCompletion endpoint, with th ChatGPT model
response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
      {"role": "user", "content": "Hello World!"}
  ])

# Extract the response
print(response.choices[0].message.content)
"""
output:
Hello there! How are you doing today?
"""