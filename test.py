import whisper

model = whisper.load_model("medium", device = "cuda")


audio_path = (r"C:\Users\gulugulu1103\OneDrive\Python\VideoTranscript\data\BV1mH4y1y72b\audios\["
              r"P1]-BV1mH4y1y72b-设计模式：简单工厂.mp3")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio(audio_path)
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized raw_text
print(result.text)