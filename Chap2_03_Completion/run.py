from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI

client = OpenAI()

# Call the openai Completion endpoint
# 不像使用 ChatCompletion，而是直接使用 Completion
response = client.completions.create(model="gpt-3.5-turbo-instruct", prompt="Hello World!")

# Extract the response
print(response.choices[0].text)
print(response)
