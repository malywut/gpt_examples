import openai

class ResponseService():
     def __init__(self):
        pass
     
     def generate_response(self, facts, user_question):
         # call the openai ChatCompletion endpoint
         response = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
         messages=[
               {"role": "user", "content": 'Based on the FACTS, give an answer to the QUESTION.'+ 
                f'QUESTION: {user_question}. FACTS: {facts}'}
            ]
         )

         # extract the response
         return (response['choices'][0]['message']['content'])