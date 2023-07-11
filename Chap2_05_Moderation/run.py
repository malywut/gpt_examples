from dotenv import load_dotenv

load_dotenv()
import openai

# Call the openai Moderation endpoint, with the text-moderation-latest model
response = openai.Moderation.create(
    model="text-moderation-latest",
    input="I want to kill my neighbor.",
)

# Extract the response
print(response)