import yt_dlp

def download_best_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',  # Saves as: video-title.extension
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Converts to audio
            'preferredcodec': 'mp3',      # You can change to 'm4a', 'wav', etc.
            'preferredquality': '192',    # You can change this too
        }],
        'quiet': False,  # Set to True to suppress output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter the video URL: ").strip()
    download_best_audio(video_url)
