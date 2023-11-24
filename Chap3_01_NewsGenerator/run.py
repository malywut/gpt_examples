from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI

client = OpenAI()
from typing import List

def ask_chatgpt(messages):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)
    return (response.choices[0].message.content)


prompt_role='You are an assistant for journalists. \
    Your task is to write articles, based on the FACTS that are given to you. \
    You should respect the instructions: the TONE, the LENGTH, and the STYLE'

def assist_journalist(facts: List[str], tone: str, length_words: int, style: str):
    facts = ", ".join(facts)
    prompt = f'{prompt_role}\nFACTS: {facts}\nTONE: {tone}\nLENGTH: {length_words} words\nSTYLE: {style}'
    return ask_chatgpt([{"role": "user", "content": prompt}])

print(assist_journalist(['The sky is blue', 'The grass is green'], 'informal', 100, 'blogpost'))