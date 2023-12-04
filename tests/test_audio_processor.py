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
		mock_stream.run.side_effect = ffmpeg.Error('mock error', stdout = b'', stderr = b'')

		# 测试extract_and_normalize_audio()方法
		result = AudioProcessor.extract_and_normalize_audio('input.mp4', 'output.wav')
		self.assertFalse(result)

		# 验证ffmpeg.input()是否被正确调用
		mock_ffmpeg.input.assert_called_once_with('input.mp4')

		# 验证ffmpeg.output()是否被正确调用
		mock_ffmpeg.input().output.assert_called_once_with('output.wav', vn = True, af = 'loudnorm')

		# 验证Stream.run()是否被正确调用
		mock_stream.run.assert_called_once()

	@patch('audio_processor.ffmpeg')
	@patch('audio_processor.logger')
	def test_split_audio_by_duration(self, mock_logger, mock_ffmpeg):
		# 创建一个模拟的Stream对象
		mock_stream = MagicMock()

		# 设置ffmpeg.input()和ffmpeg.output()的返回值
		mock_ffmpeg.input.return_value.output.return_value = mock_stream

		# 测试split_audio_by_duration()方法
		result = AudioProcessor.split_audio_by_duration('input.wav', 'output.wav', 10)
		self.assertTrue(result)

		# 验证ffmpeg.input()是否被正确调用
		mock_ffmpeg.input.assert_called_once_with('input.wav')

		# 验证ffmpeg.output()是否被正确调用
		mock_ffmpeg.input().output.assert_called_once_with('output.wav', f = 'segment', segment_time = 10)

		# 验证Stream.run()是否被正确调用
		mock_stream.run.assert_called_once()

	@patch('audio_processor.ffmpeg')
	@patch('audio_processor.logger')
	def test_split_audio_by_duration_with_error(self, mock_logger, mock_ffmpeg):
		# 创建一个模拟的Stream对象
		mock_stream = MagicMock()

		# 设置ffmpeg.input()和ffmpeg.output()的返回值
		mock_ffmpeg.input.return_value.output.return_value = mock_stream

		# 设置Stream.run()抛出异常
		mock_stream.run.side_effect = Exception('mock error')

		# 测试split_audio_by_duration()方法
		result = AudioProcessor.split_audio_by_duration('input.wav', 'output.wav', 10)
		self.assertFalse(result)

		# 验证ffmpeg.input()是否被正确调用
		mock_ffmpeg.input.assert_called_once_with('input.wav')

		# 验证ffmpeg.output()是否被正确调用
		mock_ffmpeg.input().output.assert_called_once_with('output.wav', f = 'segment', segment_time = 10)

		# 验证Stream.run()是否被正确调用
		mock_stream.run.assert_called_once()

		# 验证logger.error()是否被正确调用
		mock_logger.error.assert_called_once_with('发生错误: mock error')

	@patch('audio_processor.ffmpeg')
	@patch('audio_processor.logger')
	def test_slip_audio_by_size(self, mock_logger, mock_ffmpeg):
		# 创建一个模拟的Stream对象
		mock_stream = MagicMock()

		# 设置ffmpeg.input()和ffmpeg.output()的返回值
		mock_ffmpeg.input.return_value.output.return_value = mock_stream

		# 测试slip_audio_by_size()方法
		result = AudioProcessor.slip_audio_by_size('input.wav', 'output.wav', 1024)
		self.assertTrue(result)

		# 验证ffmpeg.input()是否被正确调用
		mock_ffmpeg.input.assert_called_once_with('input.wav')

		# 验证ffmpeg.output()是否被正确调用
		mock_ffmpeg.input().output.assert_called_once_with('output.wav', f = 'segment', segment_size = 1024)

		# 验证Stream.run()是否被正确调用
		mock_stream.run.assert_called_once()

	@patch('audio_processor.ffmpeg')
	@patch('audio_processor.logger')
	def test_slip_audio_by_size_with_error(self, mock_logger, mock_ffmpeg):
		# 创建一个模拟的Stream对象
		mock_stream = MagicMock()

		# 设置ffmpeg.input()和ffmpeg.output()的返回值
		mock_ffmpeg.input.return_value.output.return_value = mock_stream

		# 设置Stream.run()抛出异常
		mock_stream.run.side_effect = Exception('mock error')

		# 测试slip_audio_by_size()方法
		result = AudioProcessor.slip_audio_by_size('input.wav', 'output.wav', 1024)
		self.assertFalse(result)

		# 验证ffmpeg.input()是否被正确调用
		mock_ffmpeg.input.assert_called_once_with('input.wav')

		# 验证ffmpeg.output()是否被正确调用
		mock_ffmpeg.input().output.assert_called_once_with('output.wav', f = 'segment', segment_size = 1024)

		# 验证Stream.run()是否被正确调用
		mock_stream.run.assert_called_once()

		# 验证logger.error()是否被正确调用
		mock_logger.error.assert_called_once_with('发生错误: mock error')




if __name__ == '__main__':
	unittest.main()
