from pytubefix import YouTube, Playlist

def download_youtube_audio(url):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the audio stream
        audio_stream = video.streams.filter(only_audio=True).first()

        # Download the audio
        print(f"Downloading audio: {video.title}")
        audio_stream.download()
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def download_youtube_playlist(url):
    try:
        # Create a Playlist object
        playlist = Playlist(url)

        # Extract all video URLs from the playlist
        video_urls = playlist.video_urls

        # Download the audio for each video in the playlist
        for video_url in video_urls:
            download_youtube_audio(video_url)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Provide the YouTube playlist URL
playlist_url = input("Enter the YouTube playlist URL: ")
download_youtube_playlist(playlist_url)
