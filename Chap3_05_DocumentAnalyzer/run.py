from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

document_path = './files/document1.txt'
with open(document_path, 'r') as file:
    document = file.read()

    prompt = ''' You are a documentarian. Your role is to analyze documents, 
    extract the main topics, and generate a short summary. 
    Use a JSON format to provide the information, with the following structure:
    {
        "topics": ["topic1", "topic2", "topic3"],
        "summary": "The summary of the document"
    } 
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f'{prompt} Document: {document}'}],
        response_format={"type": "json_object"})
    print(response.choices[0].message.content)
