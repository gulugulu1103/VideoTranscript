import dotenv

import downloader
from VideoTranscript import VideoSet
from video_info import InfoFetcher

# 创建一个InfoFetcher对象
info_fetcher = InfoFetcher(bvid = 'BV1mH4y1y72b',
                           bili_key = dotenv.get_key('.env', 'BILI_KEY'))

video_set: VideoSet = info_fetcher.get_video_meta()

downloader.BiliDownloader.download_video_set(video_set = video_set)

