from typing import List
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def ask_chatgpt(messages):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=messages)
    return (response.choices[0].message.content)


prompt_role = '''You are an assistant for journalists. 
Your task is to write articles, based on the FACTS that are given to you. 
You should respect the instructions: the TONE, the LENGTH, and the STYLE'''


def assist_journalist(
        facts: List[str],
        tone: str, length_words: int, style: str):
    facts = ", ".join(facts)
    prompt = f'{prompt_role}\nFACTS: {facts}\nTONE: {tone}\nLENGTH: {length_words} words\nSTYLE: {style}'
    return ask_chatgpt([{"role": "user", "content": prompt}])


print(
    assist_journalist(
        ['The sky is blue', 'The grass is green'],
        'informal', 100, 'blogpost'))
"""
output:
Hey there nature lovers! Have you ever stopped to appreciate the simple beauty of the world around us? The sky is always a stunning shade of blue, providing a perfect backdrop for fluffy white clouds to float across. And let's not forget about the grass, which is a lush and vibrant green that carpets the ground beneath our feet. These two natural elements never fail to bring a sense of peace and tranquility to our hectic lives. So next time you're feeling overwhelmed, just look up at the blue sky and down at the green grass - nature's calming colors are sure to make you feel better!
"""