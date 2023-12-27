import os 
import re
from pytube import YouTube

def setup():
    if "music" not in os.listdir():
        os.mkdir("music")

def getLinks(text):
    links = list(filter(lambda line: line != "", text))
    return links

def download(links):
    os.chdir("music")
    for link in links:
        try: 
            yt = YouTube(link)
        except: 
            print(f"Error on this link\n{link}")
        else:
            # print(f"Downloading {yt.title}")
            yt.streams.get_audio_only().download()

    renameAlltoMp3()

# this is not good because 
# what if you have other files 
# in this folder, it would 
# rename it to mp3, BAD!!!
# FIXME 

def renameAlltoMp3():
    for f in os.listdir():
        sp = f.split(".")
        sp[1] = ".mp3"
        try:
            os.rename(f"{f}", f'{"".join(sp)}')
        except:
            print("Something went wrong in renameing file")

def renameToMp3(title):
    try: 
        os.rename(f"{title}.mp4", f"{title}.mp3")
    except:
        print(f"\n\nError at {title}")
        print("having issues with these types of titles")
        print("try renaming to mp3 manually\n")

def sanatizeTitle(title):
    # this is a very interesting issue
    # they are certain characters that are not allowed to include in file name
    # but they are allowed in a title of a youtube video, so i have to replace that
    
    # this does not include other alfabets or fonts in youtube titles
    # illegal = r'[^a-zA-Z0-9]' 
    # i decided not use this because there could be literally anything in the 
    # youtube title including non-ascii characters wich is a serious pain
    illegal = r'[^\w\s\.\-]'
    return re.sub(illegal, '_', title, flags=re.UNICODE)