import ffmpeg


class AudioProcessor:
	@staticmethod
	def extract_and_normalize_audio(video_path, audio_output_path):
		try:
			ffmpeg.input(video_path).output(audio_output_path, vn = True, af = 'loudnorm').run()
		except Exception as e:
			print('Error occurred: ' + str(e))
			return False
		return True
