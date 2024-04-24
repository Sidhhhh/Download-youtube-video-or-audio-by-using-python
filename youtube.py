# Download any video and audio from youtube using python 

from youtube import YouTube

# Give the video or Audio URL:-
link = YouTube('https://youtu.be/32eR_H5AdD4?feature=shared')

# Select what you want to download Video or Audio 
video = link.stream.get_audio_only()

video.download()