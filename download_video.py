from pytube import YouTube

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

# Provide the YouTube video URL
video_url = input("Enter the YouTube video URL: ")
download_youtube_video(video_url)
