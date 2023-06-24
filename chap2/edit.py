import openai

# Make sure the environment variable OPENAI_API_KEY is set.

# Call the openai Edit endpoint, with th text-davinci-edit-001 model
response = openai.Edit.create(
  model="text-davinci-edit-001",
  input="A young man is going on a trip. Before leaving, he said goodbye to his friend and parcked his suitcase.",
  instruction="Change the main character to an old woman"
)

# Extract the response
print(response['choices'][0]['text']) 