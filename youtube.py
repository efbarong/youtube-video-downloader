from pytube import YouTube

def downloadVideo(pattern, linkVideo, extension):
    if bool(pattern.match(linkVideo)):
        yt = YouTube(linkVideo)
        video = yt.streams.filter(progressive=True, file_extension=extension).order_by("resolution").desc()
        if len(video) >= 1:
            video.first().download("./videos");
            print('Video "{}" saved!'.format(yt.title))
        else:
            print("Video not available for download")
    else:
        print("Input is not a valid youtube link")