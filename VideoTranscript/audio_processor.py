import logging
import os

import ffmpeg

logger = logging.getLogger(__name__)


class AudioProcessor:
	@staticmethod
	def extract_and_normalize_audio(video_path: str, audio_output_path: str) -> bool:
		"""
		从视频中提取音频并进行音频正规化。

		:param video_path: 视频文件的路径。
		:param audio_output_path: 输出音频文件的路径。

		:return: 如果操作成功，则返回True，否则返回False。
		"""
		try:
			# af = "loudnorm"
			ffmpeg.input(video_path).output(audio_output_path, format = "mp3",
			                                acodec = 'libmp3lame',
			                                ac = 1, threads = 4, af= "loudnorm").run(overwrite_output = True)
		except Exception as e:
			logger.error('发生错误: ' + str(e))
			return False
		return True

	@staticmethod
	def split_audio_by_duration(audio_path: str, audio_segment_path: str, duration: int = 300) -> bool:
		"""
		将音频分割成指定长度的片段。

		:param audio_path: 输入音频文件的路径。
		:param audio_segment_path: 输出音频文件夹的路径。格式为segment_{i}.mp3
		:param duration: 每个片段的长度，单位为秒。

		:return: 如果操作成功，则返回True，否则返回False。
		"""
		# 确保输出目录存在
		os.makedirs(audio_segment_path, exist_ok = True)
		file_duration = AudioProcessor.get_duration(audio_path)

		for i in range(0, file_duration, duration):
			start = i
			audio_segment_filename = os.path.join(audio_segment_path, f"segment_{start // duration}.mp3")
			ffmpeg.input(audio_path).output(audio_segment_filename, acodec = 'copy', ss = start, t = duration).run(
				overwrite_output = True)
		return True

	@staticmethod
	def get_duration(video_path: str) -> int:
		"""
		获取视频的时长。

		:param video_path: 视频文件的路径。

		:return: 视频的时长，单位为秒。
		"""
		try:
			info = ffmpeg.probe(video_path)
			return int(float(info['streams'][0]['duration']))
		except Exception as e:
			logger.error('发生错误: ' + str(e))
			return -1
