import os
import json
import time
import requests
from typing import Optional
from VideoTranscript import VideoSet, VideoPart, VideoUtils


class BiliDownloader:
	@staticmethod
	def download_video_set(video_set: VideoSet, path: Optional[str] = None) -> bool:
		"""
		下载一个视频集合

		:param video_set: 视频集合
		:param path: 下载路径，默认为None，表示使用当前工作目录
		:return: 下载成功返回True，否则返回False
		"""

		# 默认下载到当前目录/data/BV号/downloads/下
		if path is None:
			path = os.path.join(os.getcwd(), "data", video_set.bvid, "downloads")

		# 如果目录不存在，就创建一个
		if not os.path.exists(path):
			os.makedirs(path)

		# 在这个目录下记录一下json
		# encoding-utf8（包含中文）
		with open(os.path.join(os.getcwd(), "data", video_set.bvid, video_set.bvid + ".json"), "w", encoding = "utf-8") as f:
			f.write(video_set.model_dump_json(indent = 4))

		for part in video_set.parts:
			if part.download_url is None:
				return False
			# [P?]-BV号-分p标题.mp4
			filename = "[P" + str(part.page) + "]-" + video_set.bvid + "-" + part.part + ".mp4"
			filename = os.path.join(path, filename)
			BiliDownloader.download_video_part(part, filename = filename)
			time.sleep(3)
		return True

	@staticmethod
	def download_video_part(part: VideoPart, filename: str, header: Optional[dict] = None) -> bool:
		"""
		下载视频分P

		:param part: 视频部分
		:param filename: 文件名
		:param header: 请求头，默认为None，表示使用默认的请求头
		:return: 下载成功返回True
		"""
		if header is None:
			header = {
				"User-Agent"     : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
				                   "Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
				"Accept"         : "application/json, raw_text/plain, */*",
				"Accept-Encoding": "gzip, deflate, br",
				"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
			}

		with requests.get(part.download_url, stream = True, headers = header) as r:
			with open(filename, "wb") as f:
				for chunk in r.iter_content(chunk_size = 1024):
					if chunk:
						f.write(chunk)

		return True
