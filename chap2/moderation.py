import openai

response = openai.Moderation.create(
    model='text-moderation-latest',
    input="I want to kill my neighbor.",
)

print(response['results'][0]['category_scores'])

