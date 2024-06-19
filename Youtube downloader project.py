from pytube import YouTube

from tkinter import *
import tkinter as tk

# Create an instance of tkinter frame or window
window = Tk()

# Set the size of the tkinter window
window.geometry("700x350")
window.title("YouTube Video Downloader")  # Give title to the window

# Function to download video
def downloader():
    # Get the video URL from the entry field
    url = url_entry.get()

    # Initialize YouTube object with the URL
    video = YouTube(url)

    # Determine the selected resolution
    if res1.get() == 1:
        resolution = '360p'
    elif res2.get() == 1:
        resolution = '720p'
    elif res3.get() == 1:
        resolution = '1080p'
    else:
        # If no resolution is selected, show an error message
        status_label.config(text="Please select a resolution.")
        return

    # Filter streams based on file extension and resolution
    video_stream = video.streams.filter(file_extension='mp4', resolution=resolution).first()

    if video_stream:
        # Download the video
        video_stream.download(filename="downloaded_video")

        # Update status label
        status_label.config(text="Download completed successfully.")
    else:
        # If no suitable stream found, show an error message
        status_label.config(text=f"No {resolution} stream available.")

# Label for the application title
Label(window, text="YOUTUBE VIDEO DOWNLOADER", bg='grey', font=('Calibri', 15)).pack(pady=10)

# Label and Entry field for URL input
Label(window, text="Enter the link to download", font=('Calibri', 12)).pack()
url_entry = Entry(window, width=50)
url_entry.pack(pady=5)

# Variables to store resolution choices
res1 = IntVar()
res2 = IntVar()
res3 = IntVar()

# Checkboxes for different resolutions
Checkbutton(window, text='360p', variable=res1, onvalue=1, offvalue=0).pack()
Checkbutton(window, text='720p', variable=res2, onvalue=1, offvalue=0).pack()
Checkbutton(window, text='1080p', variable=res3, onvalue=1, offvalue=0).pack()

# Button to trigger download
Button(window, text="Download", bg='green', command=downloader).pack(pady=10)

# Label for download status
status_label = Label(window, text="", font=('Calibri', 12))
status_label.pack()

# Start the tkinter main loop
window.mainloop()
