import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_bar['value'] = percentage_of_completion
    app.update_idletasks()


def on_complete(stream, file_path):
    download_button.config(state=tk.NORMAL)
    progress_bar['value'] = 0
    messagebox.showinfo("Download Complete", f"Video downloaded:\n{file_path}")


def download_video():
    url = url_entry.get()
    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    video_stream = yt.streams.get_highest_resolution()
    download_button.config(state=tk.DISABLED)
    video_stream.download()


app = tk.Tk()
app.title('YouTube Video Downloader')
app.geometry('400x400')
app.resizable(False, False)

frame = tk.Frame(app)
frame.pack(pady=50)

url_label = tk.Label(frame, text='Enter YouTube URL:')
url_label.pack()

url_entry = tk.Entry(frame, width=40)
url_entry.pack(pady=10)

download_button = tk.Button(frame, text='Download', command=download_video)
download_button.pack(pady=10)

progress_bar = ttk.Progressbar(frame, length=250, mode='determinate')
progress_bar.pack()

app.mainloop()
