import os 
import re
from pytube import YouTube

def setup():
    if "music" not in os.listdir():
        os.mkdir("music")

def getLinks():
    links = open("ytLinks.txt","r").read().split("\n")
    links = list(filter(lambda line: line != "", links))
    return links

def download(links):
    os.chdir("music")
    for link in links:
        try: 
            yt = YouTube(link)
        except: 
            print(f"Error on this link\n{link}")
        else:
            yt.title = sanatizeTitle(yt.title)
            print(f"Installing {yt.title}.mp3")
            yt.streams.get_audio_only().download()
            renameToMp3(yt.title)
            # yt.streams.filter(only_audio=True).first().download()

def renameToMp3(title):
    os.rename(f"{title}.mp4", f"{title}.mp3")

def sanatizeTitle(title):
    # this is a very interesting issue
    # they are certain characters that are not allowed to include in file name
    # but they are allowed in a title of a youtube video, so i have to replace that
    illegal = r'[^a-zA-Z0-9]'
    return re.sub(illegal, '_', title)
   
    return title

def main():
    setup()
    download(getLinks())

if __name__ == "__main__":
    main()
