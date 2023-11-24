from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI

client = OpenAI()

# Call the openai Completion endpoint
response = client.completions.create(model="text-davinci-003", prompt="Hello World!")

# Extract the response
print(response.choices[0].text)
