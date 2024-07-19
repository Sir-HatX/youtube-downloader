import os
from yt_dlp import YoutubeDL

def download_video(url, format_choice, resolution, save_path="."):
    if format_choice == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'postprocessor_args': [
                '-ar', '44100'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': False,
        }
    elif format_choice == "mp4":
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist(url, format_choice, resolution, save_path="."):
    if format_choice == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(save_path, '%(playlist)s/%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'postprocessor_args': [
                '-ar', '44100'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': False,
        }
    elif format_choice == "mp4":
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            'outtmpl': os.path.join(save_path, '%(playlist)s/%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()
    format_choice = input("Enter desired format (mp3 or mp4): ").strip().lower()
    resolution = input("Enter desired resolution (e.g., 720 for 720p, default is 720): ").strip() or "720"
    save_path = input("Enter the path to save the files (default is current directory): ").strip() or "."

    # Check if URL is a playlist
    is_playlist = "playlist" in url

    if is_playlist:
        download_playlist(url, format_choice, resolution, save_path)
    else:
        download_video(url, format_choice, resolution, save_path)
