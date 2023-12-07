from pydantic import BaseModel
from typing import List, Optional, Dict


class VideoPart(BaseModel):
	"""
	视频分P

	:param cid: 分P的cid
	:param page: 分P的页码
	:param part: 分P的标题
	:param duration: 分P的时长
	:param dimension: 分P的分辨率
	:param first_frame_url: 分P的第一帧的URL
	:param download_url: 分P的下载URL

	"""
	cid: int
	page: int
	part: str
	duration: int
	dimension: Dict[str, int]
	first_frame_url: str
	download_url: Optional[str] = None


class VideoSet(BaseModel):
	"""
	视频集合

	:param aid: 视频的aid
	:param bvid: 视频的bvid
	:param title: 视频的标题
	:param desc: 视频的描述
	:param part_num: 视频的分P数量
	:param parts: 视频的分P
	:param cover_url: 视频的封面URL

	"""
	aid: int
	bvid: str
	title: Optional[str] = None
	desc: Optional[str] = None
	part_num: int = 1
	parts: Optional[List[VideoPart]] = None
	cover_url: Optional[str] = None
