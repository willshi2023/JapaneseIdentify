import speech_recognition as sr

from pydub import AudioSegment

filename = r'C:\Users\shiji\PycharmProjects\JapaneseIdentify\resource\2025年2月7日 9_41_15.m4a'
# 转换m4a为wav
sound = AudioSegment.from_file(filename, format="m4a")
filename = filename + '.wav'
sound.export(filename, format="wav")

recognizer = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language="ja-JP")
print(text)
