import time

import speech_recognition as sr


def transfer_text(file_path):
    start = time.perf_counter()
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ja-JP")
    print(text)
    end = time.perf_counter()
    log_message = '录音文件识别耗费的时间：{:.2f}秒'.format(end - start)
    print(log_message)
    return log_message,text

if __name__ == '__main__':
    file_path1 = r'C:\Users\shiji\PycharmProjects\JapaneseIdentify\resource\2024年9月10日 9_20_24.m4a.wav'
    log_message,text = transfer_text(file_path1)
    print(log_message)
    print(text)