from pytube import YouTube
from pytube.cli import on_progress

link = input("Enter url:")
youtubeObject = YouTube(link,on_progress_callback=on_progress)
video = youtubeObject.streams.get_highest_resolution()
try:
    video.download()
except:
    print("Error")
print("Finished")

