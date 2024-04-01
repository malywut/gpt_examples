from openai import OpenAI

client = OpenAI()

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

    