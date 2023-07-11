from dotenv import load_dotenv

load_dotenv()
import openai

# Call the openai Edit endpoint, with the text-davinci-edit-001 model
response = openai.Edit.create(
    model="text-davinci-edit-001",
    input="A young man is going on a trip. Before leaving, he said goodbye to \
  his friend and packed his suitcase.",
    instruction="Change the main character to an old woman",
)
# extract the response
print(response["choices"][0]["text"])
