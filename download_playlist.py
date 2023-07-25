from pytube import YouTube, Playlist

def download_youtube_video(url):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the highest resolution stream available
        stream = video.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading: {video.title}")
        stream.download()
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def download_youtube_playlist(url):
    try:
        # Create a Playlist object
        playlist = Playlist(url)

        # Extract all video URLs from the playlist
        video_urls = playlist.video_urls

        # Download each video in the playlist
        for video_url in video_urls:
            download_youtube_video(video_url)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Provide the YouTube playlist URL
playlist_url = input("Enter the YouTube playlist URL: ")
download_youtube_playlist(playlist_url)
