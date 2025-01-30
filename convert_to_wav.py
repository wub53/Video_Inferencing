import moviepy
from moviepy import VideoFileClip

# Load the video file
video = VideoFileClip("1573116956_NN_WEEK1_EaseMagnesium_FIXIT_01112025_9X16.mp4")

# Extract the audio_aray and write it down to wav format
video.audio.write_audiofile("ouput_audio.wav")