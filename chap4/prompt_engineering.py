import openai

print(openai.Model.list())


print('\n1 #################\n\n')

prompt = "As Descartes said, I think therefore"
res = openai.ChatCompletion.create(
  model='gpt-4',
  messages=[        
        {'role': 'user', 'content': prompt}]
)

print('\n2 #################\n\n')

