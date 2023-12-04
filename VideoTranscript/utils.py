import json
import os
import time
from typing import Dict, Union, Optional

import requests

from data import VideoPart, VideoSet

# 定义请求头
header = {
	"User-Agent"     : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
	"Accept"         : "application/json, text/plain, */*",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5",
}


class VideoUtils:
	"""
	视频工具类，提供序列化、反序列化和下载功能
	"""

	@staticmethod
	def serialize_obj(obj: Union[VideoPart, VideoSet]) -> Dict:
		"""
		序列化VideoPart或VideoSet对象

		:param obj: VideoPart或VideoSet对象
		:return: 对象的字典表示
		"""
		if isinstance(obj, (VideoPart, VideoSet)):
			return obj.__dict__
		raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

	@staticmethod
	def deserialize_video_part(data: Dict) -> VideoPart:
		"""
		反序列化VideoPart对象

		:param data: 包含VideoPart数据的字典
		:return: VideoPart对象
		"""
		return VideoPart(**data)

	@staticmethod
	def deserialize_video_set(data: Dict) -> VideoSet:
		"""
		反序列化VideoSet对象

		:param data: 包含VideoSet数据的字典
		:return: VideoSet对象
		"""
		parts = [VideoUtils.deserialize_video_part(part_data) for part_data in data['parts']]
		return VideoSet(parts=parts, **data)


		return True