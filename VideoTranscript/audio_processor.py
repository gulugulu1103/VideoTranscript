import logging
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
            ffmpeg.input(video_path).output(audio_output_path, vn = True, af = 'loudnorm').run()
        except Exception as e:
            logger.error('发生错误: ' + str(e))
            return False
        return True

    @staticmethod
    def split_audio_by_duration(audio_path: str, output_path: str, duration: int) -> bool:
        """
		将音频分割成指定长度的片段。

		:param audio_path: 输入音频文件的路径。
		:param output_path: 输出音频文件的路径。
		:param duration: 每个片段的长度，单位为秒。

		:return: 如果操作成功，则返回True，否则返回False。
		"""
        try:
            ffmpeg.input(audio_path).output(output_path, f = 'segment', segment_time = duration).run()
        except Exception as e:
            logger.error('发生错误: ' + str(e))
            return False
        return True

    @staticmethod
    def slip_audio_by_size(audio_path: str, output_path: str, size: int) -> bool:
        """
		将音频分割成指定大小的片段。

		:param audio_path: 输入音频文件的路径。
		:param output_path: 输出音频文件的路径。
		:param size: 每个片段的大小，单位为字节。

		:return: 如果操作成功，则返回True，否则返回False。
		"""
        try:
            ffmpeg.input(audio_path).output(output_path, f = 'segment', segment_size = size).run()
        except Exception as e:
            logger.error('发生错误: ' + str(e))
            return False
        return True
