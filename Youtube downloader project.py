from pytube import YouTube

from tkinter import *
import tkinter as tk

window = Tk()

window.geometry("700x350")
window.title("YouTube Video Downloader") 

def downloader():
    url = url_entry.get()

    video = YouTube(url)

    if res1.get() == 1:
        resolution = '360p'
    elif res2.get() == 1:
        resolution = '720p'
    elif res3.get() == 1:
        resolution = '1080p'
    else:
        status_label.config(text="Please select a resolution.")
        return

    video_stream = video.streams.filter(file_extension='mp4', resolution=resolution).first()

    if video_stream:
        video_stream.download(filename="downloaded_video")

        status_label.config(text="Download completed successfully.")
    else:
        status_label.config(text=f"No {resolution} stream available.")

Label(window, text="YOUTUBE VIDEO DOWNLOADER", bg='grey', font=('Calibri', 15)).pack(pady=10)

Label(window, text="Enter the link to download", font=('Calibri', 12)).pack()
url_entry = Entry(window, width=50)
url_entry.pack(pady=5)

res1 = IntVar()
res2 = IntVar()
res3 = IntVar()

Checkbutton(window, text='360p', variable=res1, onvalue=1, offvalue=0).pack()
Checkbutton(window, text='720p', variable=res2, onvalue=1, offvalue=0).pack()
Checkbutton(window, text='1080p', variable=res3, onvalue=1, offvalue=0).pack()

Button(window, text="Download", bg='green', command=downloader).pack(pady=10)

status_label = Label(window, text="", font=('Calibri', 12))
status_label.pack()

window.mainloop()
