from pytube import YouTube


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'Downloading: {percentage_of_completion:.2f}%', end='\r', flush=True)


def on_complete(stream, file_path):
    print(f'\nDownload complete: {file_path}', flush=True)


url = input("Enter the URL of the YouTube video you want to download: ")
yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)

print("Fetching video details...")
video_stream = yt.streams.get_highest_resolution()

print(f"Downloading video: {yt.title}")
video_stream.download()
