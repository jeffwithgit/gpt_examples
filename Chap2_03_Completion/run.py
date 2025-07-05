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
"""
output:
$k, World!$k, World!
Hello
Hello World!

Completion(id='cmpl-BpywtzayHX7f7q6hZzWuIHHRT27hq', choices=[CompletionChoice(finish_reason='length', index=0, logprobs=None, text='$k, World!$k, World!\nHello\nHello World!\n')], created=1751728715, model='gpt-3.5-turbo-instruct:20230824-v2', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=16, prompt_tokens=3, total_tokens=19))
"""