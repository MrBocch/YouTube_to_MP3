import tkinter as tk
import ttkbootstrap as ttk
import time
from backend import *

def gui():

    def parseText():
        t = text.get('1.0', 'end')
        return list(filter(lambda link: link != '', t.split("\n")))
 
    def download_button():
        down_button.state(['disabled'])
        links = parseText()
        setup()
        download(links)
        down_button.state(['!disabled'])


    window = ttk.Window(themename='darkly')
    window.title("YouTube -> MP3")
    window.geometry("500x500")
    window.resizable(False, False)

    title_label = ttk.Label(master=window, text="YouTube to MP3 Converter",
                            font='Verdana 20 bold')

    title_label.pack()

    input_frame = ttk.Frame(master=window)
    down_button = ttk.Button(master=input_frame, text='Download', command=download_button)

    down_button.pack(side='left')
    input_frame.pack(pady=10)

    text = ttk.Text(window, wrap='none' ,width=50, height=20)
    text.pack()

    # output 
    output_string = tk.StringVar()
    output_lable = ttk.Label(master=window, 
                            text='output',
                            font='Calibri 24', 
                            textvariable=output_string)

    output_lable.pack(pady=10) 

    window.mainloop()

if __name__ == "__main__":
    gui()