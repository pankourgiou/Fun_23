#Install pytube module using pip install pytube command
import pytube

# Replace VIDEO_URL with the URL of the YouTube video you want to play
VIDEO_URL = "https://www.youtube.com/watch?v=um6t8pPsdCs&list=PLSBWvYm8t6uZchHi0K7auAm0Uk4wD7boi"

# Use pytube to download the video
video = pytube.YouTube(VIDEO_URL).streams.first().download()

# Play the video using the default media player
import os
os.startfile(video)
