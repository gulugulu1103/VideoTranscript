class VideoPart:
	def __init__(self, cid, page, part, duration, dimension, first_frame_url, download_url=None):
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
		self.dimension: str = dimension
		self.first_frame_url: str = first_frame_url
		self.download_url: str = download_url


class VideoSet:
	"""
	一条视频集合的信息，包括整个集合
	"""

	def __init__(self, bvid: str, title: str = None, part_num: int = 1, parts: list[VideoPart] = None, cover_url:str = None):
		"""
		一条视频集合的信息，包括整个集合
		:param bvid: 视频bv号
		:param title: 视频标题
		:param part_num: 视频分p数量
		:param parts: 视频分p信息列表
		:param cover_url: 视频封面
		"""
		self.bvid: str = bvid
		self.title: str = title
		self.part_num: int = part_num
		self.parts: list[VideoPart] = parts
		self.cover_url: str = cover_url
