from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Make sure the environment variable OPENAI_API_KEY is set.

# Call the openai ChatCompletion endpoint, with th ChatGPT model
response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"},
    messages=[{"role": "system",
               "content": "Convert the user's query in a JSON object"},
              {"role": "user",
               "content": "I am looking for blue or red shoes, leather, size 7."}])

# Extract the response
print(response.choices[0].message.content)
