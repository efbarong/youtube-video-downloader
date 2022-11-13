import re
from config import YOUTUBE_REGEX
from youtube import downloadVideo

# Configure valid youtube links
pattern = re.compile(YOUTUBE_REGEX)

# Link video input
linkVideo = input('Youtube link video:\n')

# Link validation and download
downloadVideo(pattern, linkVideo, "mp4")