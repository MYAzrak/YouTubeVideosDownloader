from pytube import YouTube

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

# Provide the YouTube video URL
video_url = input("Enter the YouTube video URL: ")
download_youtube_audio(video_url)
