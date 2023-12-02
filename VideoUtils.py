import json
import os
import requests
from VideoClass import *


class VideoUtils():
	@staticmethod
	def download_videoset(video_set: VideoSet, path: str = None) -> bool:
		"""
		下载一个视频集合
		:param video_set: 视频集合
		:param path: 下载路径
		:return: 下载成功返回True，否则返回False
		"""
		if path is None:
			path = os.getcwd()

		# 下载到/download/BV号/下
		path = os.path.join(path, "download", video_set.bvid)
		if not os.path.exists(path):
			os.makedirs(path)

		# 在这个目录下记录一下json
		# encoding-utf8（包含中文）
		with open(os.path.join(path, "video_set.json"), "w", encoding="utf8") as f:
			f.write(json.dumps(video_set.__dict__, indent=4, ensure_ascii=False))

		for part in video_set.parts:
			if part.download_url is None:
				return False
			# [P?]-BV号-分p标题.mp4
			filename = "[P" + str(part.page) + "]-" + video_set.bvid + "-" + part.part + ".mp4"
			with open(os.path.join(path, filename), "wb") as f:
				with requests.get(part.download_url, stream=True) as r:
					for chunk in r.iter_content(chunk_size=1024):
						if chunk:
							f.write(chunk)
		return True
		@staticmethod
		def download_videopage(video_page: VideoPage, path: str = None) -> bool:

			return True