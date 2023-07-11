import gradio as gr
import whisper
from dotenv import load_dotenv

load_dotenv()
import openai
model = whisper.load_model("base")


def transcribe(file):
    print(file)
    transcription = model.transcribe(file)
    return transcription['text']


prompts = {'START': 'Classify the intent of the next input. Is it: WRITE_EMAIL, QUESTION, OTHER ? Only answer one word.',
           'QUESTION': 'If you can answer the question: ANSWER, if you need more information: MORE, if you can not answer: OTHER. Only answer one word.',
           'ANSWER': 'Now answer the question',
           'MORE': 'Now ask for more information',
           'OTHER': 'Now tell me you can not answer the question or do the action',
           'WRITE_EMAIL': 'If the subject or recipient or message is missing, answer "MORE". Else if you have all the information answer "ACTION_WRITE_EMAIL | subject:subject, recipient:recipient, message:message". '}
actions = {
    'ACTION_WRITE_EMAIL':
    "The mail has been sent. Now tell me the action is done in natural language."}
messages = [{"role": "user", "content": prompts['START']}]


def generate_answer(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return (response['choices'][0]['message']['content'])


def start(user_input):
    messages.append({"role": "user", "content": user_input})
    return discussion(messages, 'START')


def discussion(messages, last_step):
    answer = generate_answer(messages)
    print(answer)
    if answer in prompts.keys():
        messages.append({"role": "assistant", "content": answer})
        messages.append({"role": "user", "content": prompts[answer]})
        return discussion(messages, answer)
    elif answer.split("|")[0].strip() in actions.keys():
        return do_action(answer)
    else:
        if last_step != 'MORE':
            messages = []
        last_step = 'END'
        return answer


def do_action(answer):
    print("Doing action " + answer)
    messages.append({"role": "assistant", "content": answer})
    action = answer.split("|")[0].strip()
    messages.append({"role": "user", "content": actions[action]})
    return discussion(messages, answer)


def start_chat(file):
    input = transcribe(file)
    print(input)
    return start(input)


gr.Interface(
    theme=gr.themes.Soft(),
    fn=start_chat,
    live=True,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs="text").launch()
