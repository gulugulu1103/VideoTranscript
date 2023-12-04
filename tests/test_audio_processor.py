import unittest
from unittest.mock import patch, MagicMock

import ffmpeg

from audio_processor import AudioProcessor


class TestAudioProcessor(unittest.TestCase):

	@patch('audio_processor.ffmpeg')
	def test_extract_and_normalize_audio(self, mock_ffmpeg):
		# 创建一个模拟的Stream对象
		mock_stream = MagicMock()

		# 设置ffmpeg.input()和ffmpeg.output()的返回值
		mock_ffmpeg.input.return_value.output.return_value = mock_stream

		# 测试extract_and_normalize_audio()方法
		result = AudioProcessor.extract_and_normalize_audio('input.mp4', 'output.wav')
		self.assertTrue(result)

		# 验证ffmpeg.input()是否被正确调用
		mock_ffmpeg.input.assert_called_once_with('input.mp4')

		# 验证ffmpeg.output()是否被正确调用
		mock_ffmpeg.input().output.assert_called_once_with('output.wav', vn = True, af = 'loudnorm')

		# 验证Stream.run()是否被正确调用
		mock_stream.run.assert_called_once()

	@patch('audio_processor.ffmpeg')
	def test_extract_and_normalize_audio_with_error(self, mock_ffmpeg):
		# 创建一个模拟的Stream对象
		mock_stream = MagicMock()

		# 设置ffmpeg.input()和ffmpeg.output()的返回值
		mock_ffmpeg.input.return_value.output.return_value = mock_stream

		# 设置Stream.run()抛出异常
		mock_stream.run.side_effect = ffmpeg.Error('mock error', stdout=b'', stderr=b'')

		# 测试extract_and_normalize_audio()方法
		result = AudioProcessor.extract_and_normalize_audio('input.mp4', 'output.wav')
		self.assertFalse(result)

		# 验证ffmpeg.input()是否被正确调用
		mock_ffmpeg.input.assert_called_once_with('input.mp4')

		# 验证ffmpeg.output()是否被正确调用
		mock_ffmpeg.input().output.assert_called_once_with('output.wav', vn = True, af = 'loudnorm')

		# 验证Stream.run()是否被正确调用
		mock_stream.run.assert_called_once()


if __name__ == '__main__':
	unittest.main()
