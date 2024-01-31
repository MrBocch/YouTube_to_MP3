import os 
import re
from pytube import YouTube

def setup():
    if "ytb2mp3_music" not in os.listdir():
        os.mkdir("ytb2mp3_music")

def getLinks(text):
    links = list(filter(lambda line: line != "", text))
    return links

def download(links):
    os.chdir("ytb2mp3_music")
    failed = []
    for link in links:
        try: 
            yt = YouTube(link)
        except: 
            failed.append(link)
            print(f"Error on this link\n{link}")
        
        try:
            yt.streams.get_audio_only().download()
        except:
            failed.append(link)
            print("by pass age restricted videos somehow")

    renameAlltoMp3()
    os.chdir("..")

    return failed

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