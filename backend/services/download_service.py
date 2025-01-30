import whisper
import os
import hashlib
from pytube import YouTube

model_name = "tiny.en"  
model = whisper.load_model(model_name)


def download_video(url):
    yt = YouTube(url)
    hash_file = hashlib.md5()
    hash_file.update(yt.title.encode())
    file_name = f'{hash_file.hexdigest()}.mp4'
    yt.streams.first().download(output_path=os.getcwd(), filename=file_name)

    return {
        "file_name": file_name,
        "title": yt.title
    }

def transcribe_yt(url):
    try:
        vid=download_video(url)
        result = model.transcribe(vid["file_name"])
        os.remove(vid["file_name"])

        segments = []
        for item in result["segments"]:
            segments.append(convert_segment(item))

        return {
            "title": vid["title"],
            "segments": segments
        }
   
    except Exception as e:
        raise Exception(f"Error transcribiendo el video: {str(e)}")


def convert_segment(segment):
    return {
        "start": segment["start"],
        "text": segment["text"]
    }