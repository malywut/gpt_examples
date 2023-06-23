from dotenv import load_dotenv

load_dotenv()
import openai

# Call the openai Completion endpoint
response = openai.Completion.create(
    model="text-davinci-003", prompt="Hello World!"
)

# Extract the response
print(response["choices"][0]["text"])
