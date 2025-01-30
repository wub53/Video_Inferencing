# TRy the Below  ----------------------------------------------------------------------------------------------------------------------------
import base64
from openai import OpenAI

client = OpenAI()

# CONVERT AUDIO TO WAV format

from moviepy import VideoFileClip

# # Load the video file
# video = VideoFileClip("1573116956_NN_WEEK1_EaseMagnesium_FIXIT_01112025_9X16.mp4")

# # Extract the audio_aray and write it down to wav format
# video.audio.write_audiofile("output_audio.wav")

def read_audio_file(filepath: str):
    with open(filepath, "rb") as audio_file:
        return audio_file.read()

# Read and encode the audio data(which should be in wav format) as base64
audio_data = read_audio_file("/Users/omkarpatil/FluxCap/Video_Inferencing_MultiModalLLM/ouput_audio.wav")
encoded_string = base64.b64encode(audio_data).decode("utf-8")

# Send the encoded audio as base64 string in the `input_audio`    "API EXECUTION TIME 18 SECONDS" 
completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text"],
    messages=[
        {
            "role": "system",
            "content": "Your job is to read the audio stream carefully ",
        },
        {
            "role": "user",
            "content": [
                { 
                    "type": "text",
                    "text": "generate a detailed and accurate transcript of it"
                },
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": encoded_string,  # Use the base64 string here
                        "format": "wav",
                    },
                }
            ],
        },
    ],
)

# Print the response
print(completion.choices[0].message.content)

# Response: "The tone of the recording is calm, instructive, and soothing. 
# The speaker uses a relaxed and gentle manner to guide listeners through a breathing exercise, aiming to help them achieve a state of relaxation and calmness.."