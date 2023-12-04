from openai import OpenAI
client = OpenAI()

audio_file= open("/path/to/file/audio.mp3", "rb")
transcript = client.audio.transcriptions.create(
		model = "model_7qZ2Z5X4",
)