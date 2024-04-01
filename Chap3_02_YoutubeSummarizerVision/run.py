
from openai import OpenAI
from dotenv import load_dotenv
import base64
import cv2
load_dotenv()

client = OpenAI()

# Open the video file or read from URL
video = cv2.VideoCapture("files/video.mp4")

# Extract the frames from the video
base64Frames = []
i=0
while video.isOpened():
    success, frame = video.read()
    i+=1
    if not success or i>5:
        break
    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

video.release()

# Create the object to send to OpenAI. We will send the first 10 frames as a list of base64 strings
images = [{"image": frame, "resize":768} for frame in base64Frames[2::3]]

# Call the openai chat endpoint, with the GPT-4 vision model
response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    max_tokens= 200,
    messages=[{"role": "user", "content": ["These are the frames from a video. Generate a two sentence summary.", *images]}    
    ])


print(response.choices[0].message.content)
