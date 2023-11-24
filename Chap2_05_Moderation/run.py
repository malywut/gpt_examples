from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI

client = OpenAI()

# Call the openai Moderation endpoint, with the text-moderation-latest model
response = client.moderations.create(model="text-moderation-latest",
input="I want to kill my neighbor.")

# Extract the response
print(response)