'''
This is a Youtube Video Downloader.

Prerequsties:
1) Make sure pytube is installed in your system.

If not, install using -  pip install pytube  in cmd.

Author: Satender Jangra
For any issue you can connect with me on - satender0095@gmail.com
'''


#import YoutTube from pytube
from pytube import YouTube

try:
    video_link = input('Enter youtube link: ')           #Get link of the video, you want to download 
    video = YouTube(video_link)
    path = input('Enter path: ')                           #Enter your path where you want to download it
    print('Processing')
    video.streams.filter(res='720p').first().download(path)        #downloading the video 
    print('Completed')
except:
    print('Enter Valid link')

