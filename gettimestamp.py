import whisper
import os

audio_file = "Big Cities.mp3"

model = whisper.load_model("base")

result = model.transcribe(audio_file, word_timestamps=True)

output_file = os.path.splitext(audio_file)[0] + ".txt"

with open(output_file, "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        f.write(f"[{segment['start']:.2f}s - {segment['end']:.2f}s] {segment['text']}\n")

print(f"Kết quả đã được lưu vào: {output_file}")
