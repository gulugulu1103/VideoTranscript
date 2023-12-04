import unittest
from downloader import BiliDownloader
from unittest.mock import patch, MagicMock, ANY
import tempfile
import os


class TestBiliDownloader(unittest.TestCase):

	# @patch('downloader.BiliDownloader.download_videopart')
	# @patch('downloader.os')
	# @patch('downloader.json')
	# @patch('downloader.time')
	# def test_download_videoset(self, mock_time, mock_json, mock_os, mock_download_videopart):
	# 	# 创建一个模拟的VideoSet对象
	# 	mock_video_set = MagicMock()
	# 	mock_video_set.bvid = 'mock_bvid'
	# 	mock_video_set.parts = [MagicMock()]
	#
	# 	# 创建一个临时目录
	# 	with tempfile.TemporaryDirectory() as tmpdirname:
	# 		# 设置os.getcwd()的返回值为临时目录的路径
	# 		mock_os.getcwd.return_value = tmpdirname
	#
	# 		# 设置os.path.join()的返回值
	# 		mock_os.path.join.return_value = os.path.join(tmpdirname, 'downloads', mock_video_set.bvid)
	#
	# 		# 设置os.path.exists()的返回值
	# 		mock_os.path.exists.return_value = False
	#
	# 		# 设置json.dumps()的返回值
	# 		mock_json.dumps.return_value = 'mock_json_string'
	#
	# 		# 设置download_videopart()的返回值
	# 		mock_download_videopart.return_value = True
	#
	# 		# 测试download_videoset()方法
	# 		result = BiliDownloader.download_videoset(mock_video_set)
	# 		self.assertTrue(result)
	#
	# 		# 验证os.getcwd()是否被正确调用
	# 		mock_os.getcwd.assert_called_once()
	#
	# 		# 验证os.path.exists()是否被正确调用
	# 		mock_os.path.exists.assert_called_once_with(os.path.join(tmpdirname, 'downloads', mock_video_set.bvid))
	#
	# 		# 验证os.makedirs()是否被正确调用
	# 		mock_os.makedirs.assert_called_once_with(os.path.join(tmpdirname, 'downloads', mock_video_set.bvid))
	#
	# 		# 验证json.dumps()是否被正确调用
	# 		mock_json.dumps.assert_called_once()
	#
	# 		# 验证download_videopart()是否被正确调用
	# 		mock_download_videopart.assert_called()
	#
	# 		# 验证time.sleep()是否被正确调用
	# 		mock_time.sleep.assert_called_with(3)

	@patch('downloader.requests')
	def test_download_videopart(self, mock_requests):
		# 创建一个模拟的VideoPart对象
		mock_video_part = MagicMock()
		mock_video_part.download_url = 'http://mock.url'  # 修改这里

		# 创建一个模拟的Response对象
		mock_response = MagicMock()
		mock_response.iter_content.return_value = [b'mock_chunk']

		# 设置requests.get()的返回值
		mock_requests.get.return_value.__enter__.return_value = mock_response

		# 测试download_videopart()方法
		result = BiliDownloader.download_videopart(mock_video_part, 'mock_filename')
		self.assertTrue(result)

		# 验证requests.get()是否被正确调用
		mock_requests.get.assert_called_once_with('http://mock.url', stream = True, headers = ANY)


if __name__ == '__main__':
	unittest.main()
