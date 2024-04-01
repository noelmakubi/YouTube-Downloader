from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the video you want to download: ")
    download_video(url)
