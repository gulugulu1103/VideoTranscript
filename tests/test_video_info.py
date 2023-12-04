import unittest
from video_info import InfoFetcher
from unittest.mock import patch, MagicMock
import dotenv


class TestInfoFetcher(unittest.TestCase):

	def setUp(self):
		self.BV = 'mock_bv'
		self.bili_key = 'mock_bili_key'
		self.header = { 'mock_header': 'mock_value' }
		self.info_fetcher = InfoFetcher(self.BV, self.bili_key, self.header)

	@patch('video_info.requests')
	def test_get_video_meta(self, mock_requests):
		# 创建一个模拟的Response对象
		mock_response = MagicMock()
		mock_response.json.return_value = { 'mock_key': 'mock_value' }

		# 设置requests.get()的返回值
		mock_requests.get.return_value = mock_response

		# 测试get_video_meta()方法
		result = self.info_fetcher.get_video_meta()
		self.assertEqual(result, { 'mock_key': 'mock_value' })

		# 验证requests.get()是否被正确调用
		mock_requests.get.assert_called_once_with("https://bili.zhouql.vip/meta/" + self.BV, headers = self.header)

	@patch('video_info.requests')
	def test_get_download_urls(self, mock_requests):
		# 创建一个模拟的VideoSet对象
		mock_video_set = MagicMock()
		mock_video_set.aid = 'mock_aid'
		mock_video_set.parts = [MagicMock()]

		# 创建一个模拟的Response对象
		mock_response = MagicMock()
		mock_response.json.return_value = { 'data': { 'durl': [{ 'url': 'mock_url' }] } }

		# 设置requests.get()的返回值
		mock_requests.get.return_value = mock_response

		# 测试get_download_urls()方法
		self.info_fetcher.get_download_urls(mock_video_set)

		# 验证requests.get()是否被正确调用
		mock_requests.get.assert_called_once_with(
			"https://bili.zhouql.vip/download/" + str(mock_video_set.aid) + "/" + str(mock_video_set.parts[0].cid),
			headers = self.header)


if __name__ == '__main__':
	unittest.main()
