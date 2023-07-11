from dotenv import load_dotenv

load_dotenv()
import openai

# For GPT 3.5 Turbo, the endpoint is ChatCompletion
response = openai.ChatCompletion.create(
    # For GPT 3.5 Turbo, the model is “gpt-3.5-turbo”
    model="gpt-3.5-turbo",
    # Conversation as a list of messages.
    messages=[
        {"role": "system", "content": "You are a helpful teacher."},
        {
            "role": "user",
            "content": "Is there other measures than time complexity for an \
            algorithm?",
        },
        {
            "role": "assistant",
            "content": "Yes, there are other measures besides time complexity \
            for an algorithm, such as space complexity.",
        },
        {"role": "user", "content": "What is it?"},
    ],
)

print (response["choices"][0]["message"]["content"])