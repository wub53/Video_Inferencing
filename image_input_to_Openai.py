from dotenv import load_dotenv
from openai import OpenAI
import cv2
import base64
import os

load_dotenv()

frames_skipper = 0

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
video = cv2.VideoCapture("1573116956_NN_WEEK1_EaseMagnesium_FIXIT_01112025_9X16.mp4")

 # Get the total number of frames
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

if total_frames <= 1000:
    frames_skipper = 30
if total_frames > 1000 and total_frames <= 1500:
    frames_skipper = 45
if total_frames > 1500 and total_frames <= 2000:
    frames_skipper = 60
if total_frames > 2000 and total_frames <= 3000:
    frames_skipper = 90


#Extract frames from video
base64Frames = []
while video.isOpened():
    success, frame = video.read()
    if not success:
        break
    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

video.release()
print(len(base64Frames), "frames read.\n")

#Call the opan AI 6 times according to the number of empty spaces in the JSON object

# Create chat prompt
SUPER_PROMPT_MESSAGES = [
    
    {
        "role": "user",
        "content": [         
            *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::frames_skipper]),
            "Analyze the above image frames of a digital marketing advertisement and give the detailed description of the ad. ",
            
        ],
    },
    
]

params = {
    "model": "gpt-4o",
    "messages": SUPER_PROMPT_MESSAGES,
    "max_tokens": 3000,
}

result = client.chat.completions.create(**params)

print(type(result))

print(result.choices[0].message.content)

# To Do : 
# For concept , we would want to see the whole summary of transcript 