import logging
import time
from typing import List

import dotenv
import requests

import downloader
from data import VideoPart, VideoSet


class InfoFetcher:
	def __init__(self, bvid: str, bili_key: str = None, header: dict = None):
		"""
		初始化BiliDownloader类

		:param bvid: Bilibili视频的BV号
		:param bili_key: Bilibili API的key
		:param header: 请求头，用于模拟浏览器

		"""
		self.BV = bvid
		self.bili_key = bili_key
		if bili_key is None:
			self.bili_key = dotenv.get_key(".env", "BILI_KEY")
		self.header = header
		if header is None:
			self.header = {
				"User-Agent"     : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
				                   "Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
				"Accept"         : "application/json, raw_text/plain, */*",
				"Accept-Encoding": "gzip, deflate, br",
				"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
			}
		self.logger = logging.getLogger(__name__)

	def get_video_meta(self) -> VideoSet:
		"""
		获取视频元数据

		:return: 包含视频元数据的字典
		"""
		self.logger.info("正在获取视频元数据...")
		response = requests.get("https://bili.zhouql.vip/meta/" + self.BV, headers = self.header)
		response.encoding = 'utf-8'
		self.logger.info("获取视频元数据成功！")
		j = response.json()
		self.logger.debug("获取到json from API：" + str(j))
		video_set = VideoSet(
				aid = j["data"]["aid"],
				bvid = j["data"]["bvid"],
				title = j["data"]["title"],
				desc = j["data"]["desc"],
				part_num = j["data"]["videos"],
				cover_url = j["data"]["pic"]
		)
		self.logger.debug("获取到视频元数据：" + str(video_set))
		self.logger.info("正在获取视频分P...")
		video_set.parts = self.get_video_parts(j)
		self.logger.info("获取视频分P成功！（未获取下载链接）")
		self.logger.debug("获取到视频分P：" + str(video_set.parts))
		self.logger.info("正在获取下载链接...")
		self.get_download_urls(video_set)
		self.logger.info("获取下载链接成功！")

		return video_set

	def get_video_parts(self, j: dict) -> List[VideoPart]:
		"""
		获取视频各分P的信息

		:param j: 包含视频元数据的字典
		:return: VideoPart对象的列表
		"""
		parts = []
		for each in j["data"]["pages"]:
			new_part = VideoPart(
					cid = each["cid"],
					page = each["page"],
					part = each["part"],
					duration = each["duration"],
					dimension = each["dimension"],
					first_frame_url = each["first_frame"],
					download_url = None
			)
			self.logger.debug("获取到分P：" + str(new_part))
			self.logger.info("获取到第" + str(new_part.page) + "P：" + str(new_part.part))
			parts.append(new_part)

		return parts

	def get_download_urls(self, video_set: VideoSet):
		"""
		获取下载链接

		:param video_set: VideoSet对象
		"""
		for each in video_set.parts:
			response = requests.get("https://bili.zhouql.vip/download/" + str(video_set.aid) + "/" + str(each.cid),
			                        headers = self.header)
			response.encoding = 'utf-8'
			j = response.json()
			each.download_url = j["data"]["durl"][0]["url"]
			time.sleep(3)
			self.logger.info("获取到第" + str(each.page) + "P的下载链接：" + str(each.download_url))
		self.logger.info("获取下载链接成功！")
