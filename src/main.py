import sys
from gui import *
from backend import *

def climode():
    links = []
    print("Enter youtube links")
    print("just press enter to leave")

    while True:
        link = input("> ")

        if link == "":
            return links

        links.append(link)

def filemode(file):
    links = None
    try:
        with open(file, "r") as f:
            links = f.readlines()
    except:
        print(f"could not open file \"{file}\"")

    return links

if __name__ == "__main__":
    if len(sys.argv) == 1:
        gui()
        pass
    else:
        if sys.argv[1] in ["help", "--help", "-h"]:
            print("YouTube2MP3 app")
            print("Print version")
            print("--version")
            print("-v\n")

            print("Read from file")
            print("--file file.txt")
            print("-f file.txt\n")

            print("CLI version")
            print("--cli")
            print("-c")

        elif sys.argv[1] in ["--version", "-v"]:
            print("YouTube2MP3 0.0.1")

        elif sys.argv[1] in ["--file", "-f"]:
            if len(sys.argv) == 2:
                print("Enter name of file")
                exit()

            # maybe should delete clean the links?
            links = filemode(sys.argv[2])
            setup()
            failed = download(links)

            if len(failed) == 0:
                print("All done")
            else:
                print("Failed to download these due to reasons")
                for f in failed:
                    print(f)

        elif sys.argv[1] in ["--cli", "-c"]:
            links = climode()
            setup()
            failed = download(links)

            if len(failed) == 0:
                print("All done")
            else:
                print("Failed to download these due to reasons")
                for f in failed:
                    print(f)
