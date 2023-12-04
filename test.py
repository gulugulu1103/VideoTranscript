import os

import dotenv
from openai import OpenAI

import audio_processor


class Transcripter:
	def __init__(self, bvid, segment_length):
		self.bvid = bvid
		self.segment_length = segment_length
		self.api_key = dotenv.get_key(".env", "OPENAI_KEY")
		self.client = OpenAI(api_key = self.api_key, base_url = "https://orisound.cn/v1")

	def set_paths(self, file_name):
		self.file = f"./data/{self.bvid}/downloads/{file_name}"
		self.audio_file = f"./data/{self.bvid}/audios/{file_name}.mp3"
		self.transcript_file = f"./data/{self.bvid}/transcriptions/{file_name}.txt"
		self.part_name = os.path.splitext(os.path.basename(self.file))[0]
		self.segments_path = os.path.join(f"./data/{self.bvid}/segments/", self.part_name)

	def process_audio(self):
		if not os.path.exists(self.audio_file):
			os.makedirs(os.path.dirname(self.audio_file), exist_ok = True)
		duration = audio_processor.AudioProcessor.get_duration(self.file)
		audio_processor.AudioProcessor.extract_and_normalize_audio(self.file, self.audio_file)
		os.makedirs(self.segments_path, exist_ok = True)
		audio_processor.AudioProcessor.split_audio_by_duration(self.audio_file, self.segments_path, self.segment_length)

	def transcribe(self):
		if not os.path.exists(self.transcript_file):
			os.makedirs(os.path.dirname(self.transcript_file), exist_ok = True)
		for segment_audio in os.listdir(self.segments_path):
			print("正在处理：" + segment_audio)
			with open(os.path.join(self.segments_path, segment_audio), "rb") as f:
				transcript = self.client.audio.transcriptions.create(
						model = "whisper-1",
						file = f,
						response_format = "json"
				)
			with open(self.transcript_file, "a", encoding = 'utf-8') as f:
				f.write(transcript.text)

	def process(self, file_name):
		self.set_paths(file_name)
		self.process_audio()
		self.transcribe()


transcripter = Transcripter("BV1mH4y1y72b", 300)
for file in os.listdir(f"./data/{transcripter.bvid}/downloads/"):
	transcripter.process(file)
