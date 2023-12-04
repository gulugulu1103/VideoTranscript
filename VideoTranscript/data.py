import json
import os
import requests
from typing import List, Optional, Dict


class VideoPart:
	def __init__(self, cid: int, page: int, part: str, duration: int, dimension: Dict[str, int], first_frame_url: str,
	             download_url: Optional[str] = None):
		"""
		一条视频
		:param cid: 视频cid
		:param page: 视频分p名称
		:param part: 视频标题
		:param duration: 视频时长
		:param dimension: 视频分辨率
		:param first_frame_url: 视频第一帧
		:param download_url: 视频下载地址
		"""
		self.cid: int = cid
		self.page: int = page
		self.part: str = part
		self.duration: int = duration
		self.dimension: Dict[str, int] = dimension
		self.first_frame_url: str = first_frame_url
		self.download_url: Optional[str] = download_url


class VideoSet:
	"""
	一条视频集合的信息，包括整个集合
	"""

	def __init__(self, aid: int, bvid: str, title: Optional[str] = None, desc: Optional[str] = None, part_num: int = 1,
	             parts: Optional[List[VideoPart]] = None,
	             cover_url: Optional[str] = None):
		"""
		一条视频集合的信息，包括整个集合
		:param aid: 视频aid
		:param bvid: 视频bv号
		:param title: 视频标题
		:param desc: 视频简介
		:param part_num: 视频分p数量
		:param parts: 视频分p信息列表
		:param cover_url: 视频封面

		"""
		self.aid: int = aid
		self.bvid: str = bvid
		self.title: Optional[str] = title
		self.desc: Optional[str] = desc
		self.part_num: int = part_num
		self.parts: Optional[List[VideoPart]] = parts
		self.cover_url: Optional[str] = cover_url
