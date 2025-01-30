import whisper
import os
import hashlib
from pytube import YouTube

model_name = "tiny"  # Whisper model to use
model = whisper.load_model(model_name)


def download_video(url):
    yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    print(yt.title)
    
    return {
        "file_name": "file_name",
        "title": yt.title
    }


def transcribe_yt(url):
    video = download_video(url)
    result = model.transcribe(video["file_name"])
    os.remove(video["file_name"])

    segments = []
    for item in result["segments"]:
        segments.append(format_item(item))

    return {
        "title": video["title"],
        "segments": segments
    }


def format_item(item):
    return {
        "time": item["start"],
        "text": item["text"]
    }