import unittest
from data import VideoSet, VideoPart


class TestVideoSet(unittest.TestCase):

	def setUp(self):
		self.aid = 123
		self.bvid = 'BV1K7411d7dE'
		self.title = 'Test Video'
		self.desc = 'This is a test video'
		self.part_num = 1
		self.parts = None
		self.cover_url = 'http://example.com/cover.jpg'

		self.video_set = VideoSet(
				aid = self.aid,
				bvid = self.bvid,
				title = self.title,
				desc = self.desc,
				part_num = self.part_num,
				parts = self.parts,
				cover_url = self.cover_url
		)

	def test_init(self):
		self.assertEqual(self.video_set.aid, self.aid)
		self.assertEqual(self.video_set.bvid, self.bvid)
		self.assertEqual(self.video_set.title, self.title)
		self.assertEqual(self.video_set.desc, self.desc)
		self.assertEqual(self.video_set.part_num, self.part_num)
		self.assertEqual(self.video_set.parts, self.parts)
		self.assertEqual(self.video_set.cover_url, self.cover_url)


class TestVideoPart(unittest.TestCase):

	def setUp(self):
		self.cid = 123
		self.page = 1
		self.part = 'Part 1'
		self.duration = 60
		self.dimension = { 'width': 1280, 'height': 720 }
		self.first_frame_url = 'http://example.com/first_frame.jpg'
		self.download_url = 'http://example.com/download.mp4'

		self.video_part = VideoPart(
				cid = self.cid,
				page = self.page,
				part = self.part,
				duration = self.duration,
				dimension = self.dimension,
				first_frame_url = self.first_frame_url,
				download_url = self.download_url
		)

	def test_init(self):
		self.assertEqual(self.video_part.cid, self.cid)
		self.assertEqual(self.video_part.page, self.page)
		self.assertEqual(self.video_part.part, self.part)
		self.assertEqual(self.video_part.duration, self.duration)
		self.assertEqual(self.video_part.dimension, self.dimension)
		self.assertEqual(self.video_part.first_frame_url, self.first_frame_url)
		self.assertEqual(self.video_part.download_url, self.download_url)


if __name__ == '__main__':
	unittest.main()
