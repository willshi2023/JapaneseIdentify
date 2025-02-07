import speech_recognition as sr
import time
from pydub import AudioSegment


filename = r'C:\Users\shiji\PycharmProjects\JapaneseIdentify\resource\2024年9月10日 9_20_24.m4a'
start = time.perf_counter()
# 转换m4a为wav
sound = AudioSegment.from_file(filename, format="m4a")
filename = filename + '.wav'
sound.export(filename, format="wav")
end = time.perf_counter()
print('录音文件格式转换耗费的时间：{:.2f}秒'.format(end - start))

start = time.perf_counter()
recognizer = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language="ja-JP")
print(text)
end = time.perf_counter()
print('录音文件识别耗费的时间：{:.2f}秒'.format(end - start))