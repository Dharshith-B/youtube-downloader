import os
import yt_dlp
import subprocess

# User inputs
url = input("📺 Enter YouTube URL: ").strip()
quality = input("🎞️ Desired video quality (e.g., 720): ").strip()
filename = input("💾 Base filename (without extension): ").strip()

video_file = f"{filename}_video.mp4"
audio_file = f"{filename}_audio.m4a"
output_file = f"{filename}.mp4"
subtitle_file = f"{filename}.srt"

def download_format(url, format_selector, out_file):
    ydl_opts = {
        'format': format_selector,
        'outtmpl': out_file,
        'quiet': False,
        'noplaylist': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_subtitles(lang='en', auto=False):
    print(f"📝 Trying {'auto-' if auto else ''}captions...")
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': not auto,
        'writeautomaticsub': auto,
        'subtitleslangs': [lang],
        'subtitlesformat': 'srt',
        'outtmpl': f"{filename}.%(ext)s",
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # Check subtitle file
        if os.path.exists(subtitle_file):
            print("✅ Subtitles downloaded")
            return True
        else:
            return False

print("⬇️ Downloading video...")
download_format(url, f"bv[height<={quality}]", video_file)

print("⬇️ Downloading audio...")
download_format(url, "ba", audio_file)

print("🧪 Attempting to get subtitles...")
subs_downloaded = download_subtitles()
if not subs_downloaded:
    subs_downloaded = download_subtitles(auto=True)

print("🔀 Merging video and audio...")
subprocess.run([
    "ffmpeg",
    "-i", video_file,
    "-i", audio_file,
    "-c:v", "copy",
    "-c:a", "aac",
    "-y", output_file
], check=True)

# Clean up temp files
os.remove(video_file)
os.remove(audio_file)

print("\n🎉 Finished!")
print(f"📹 Video saved as: {output_file}")
print(f"📝 Subtitles: {'available' if subs_downloaded else 'not available'} ({subtitle_file if subs_downloaded else 'N/A'})")
