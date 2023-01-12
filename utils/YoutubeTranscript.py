from transformers import pipeline 
from youtube_transcript_api import YouTubeTranscriptApi

def Generate_yt_transcript(video_link):
    video_id = video_link.split("=")[1]  
    video_id = video_id[0:11]

    transcript = YouTubeTranscriptApi.get_transcript(video_id) 

    gen_transcript = ""     
    for i in transcript:
        gen_transcript += ' ' + i['text']

    return gen_transcript