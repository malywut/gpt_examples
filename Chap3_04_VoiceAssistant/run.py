import gradio as gr
import whisper
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

starting_prompt = """You are an assistant.
You can discuss with the user, or perform email tasks. Emails require subject, recipient, and body.
You will receive either intructions starting with [Instruction] , or user input starting with [User]. Follow the instructions.
"""

prompts = {'START': '[Instruction] Write WRITE_EMAIL if the user wants to write an email, "QUESTION" if the user has a precise question, "OTHER"  in any other case. Only write one word.',
           'QUESTION': '[Instruction] If you can answer the question, write "ANSWER", if you need more information write MORE, if you cannot answer write "OTHER". Only write one word.',
           'ANSWER': '[Instruction] Answer the user''s question',
           'MORE': '[Instruction] Ask the user for more information as specified by previous intructions',
           'OTHER': '[Instruction] Give a polite answer or greetings if the user is making polite conversation. Else, answer to the user that you cannot answer the question or do the action',
           'WRITE_EMAIL': '[Instruction] If the subject or recipient or body is missing,  answer "MORE". Else if you have all the information answer "ACTION_WRITE_EMAIL | subject:subject, recipient:recipient, message:message". ',
           'ACTION_WRITE_EMAIL': '[Instruction] The mail has been sent. Answer to the user to  tell the action is done'}
actions = ['ACTION_WRITE_EMAIL']


class Discussion:
    """
    A class representing a discussion with a voice assistant.

    Attributes:
        state (str): The current state of the discussion.
        messages_history (list): A list of dictionaries representing the history of messages in the discussion.
        client: An instance of the OpenAI client.
        stt_model: The speech-to-text model used for transcribing audio.

    Methods:
        generate_answer: Generates an answer based on the given messages.
        reset: Resets the discussion to the initial state.
        do_action: Performs the specified action.
        transcribe: Transcribes the given audio file.
        discuss_from_audio: Starts a discussion based on the transcribed audio file.
        discuss: Continues the discussion based on the given input.
    """

    def __init__(
            self, state='START',
            messages_history=[{'role': 'user',
                               'content': f'{starting_prompt}'}]) -> None:
        self.state = state
        self.messages_history = messages_history
        self.client = OpenAI()
        self.stt_model = whisper.load_model("base")
        pass

    def generate_answer(self, messages):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages)
        return (response.choices[0].message.content)

    def reset(self, start_state='START'):
        self.messages_history = [
            {'role': 'user', 'content': f'{starting_prompt}'}]
        self.state = start_state
        self.previous_state = None

    def reset_to_previous_state(self):
        self.state = self.previous_state
        self.previous_state = None

    def to_state(self, state):
        self.previous_state = self.state
        self.state = state

    def do_action(self, action):
        """
        Performs the specified action.

        Args:
            action (str): The action to perform.
        """
        print(f'DEBUG perform action={action}')
        pass

    def transcribe(self, file):
        transcription = self.stt_model.transcribe(file)
        return transcription['text']

    def discuss_from_audio(self, file):
        if file:
            # Transcribe the audio file and use the input to start the discussion
            return self.discuss(f'[User] {self.transcribe(file)}')
        # Empty output if there is no file
        return ''

    def discuss(self, input=None):
        if input is not None:
            self.messages_history.append({"role": "user", "content": input})

        # Generate a completion
        completion = self.generate_answer(
            self.messages_history +
            [{"role": "user", "content": prompts[self.state]}])

        # Is the completion an action ?
        if completion.split("|")[0].strip() in actions:
            action = completion.split("|")[0].strip()
            self.to_state(action)
            self.do_action(completion)
            # Continue discussion
            return self.discuss()
        # Is the completion a new state ?
        elif completion in prompts:
            self.to_state(completion)
            # Continue discussion
            return self.discuss()
        # Is the completion an output for the user ?
        else:
            self.messages_history.append(
                {"role": "assistant", "content": completion})
            if self.state != 'MORE':
                # Get back to start
                self.reset()
            else:
                # Get back to previous state
                self.reset_to_previous_state()
            return completion


if __name__ == '__main__':
    discussion = Discussion()

    gr.Interface(
        theme=gr.themes.Soft(),
        fn=discussion.discuss_from_audio,
        live=True,
        inputs=gr.Audio(sources="microphone", type="filepath"),
        outputs="text").launch()

    # To use command line instead of Gradio, remove above code and use this instead:
    # while True:
    #     message = input('User: ')
    #     print(f'Assistant: {discussion.discuss(message)}')