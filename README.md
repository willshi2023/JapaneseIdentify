## telegram交流群 
https://t.me/languageidentify
## 说明
程序可以利用电报进行日语音频转日语文字，支持录音和直接语音，完全免费  

这个程序的灵感来自日语学习，平时生活或者工作中，遇到听不懂的日语，比如在电车上突然插播紧急信息，或者工作中开会突然遇到听不懂的日语，这个时候直接录下来，就知道意思，以后再遇到相同的单词，就能立马听懂。程序完全免费，可以自己搭建，也可以直接加入交流群，无需代码即可体验
## 安装所需库

```
Python版本3.12
pip install SpeechRecognition
pip install pydub
pip install python-telegram-bot
pip install requests

```

## 安装 FFmpeg

在 Windows 上，你可以下载 FFmpeg 并将其添加到系统的 PATH 环境变量中。

1. 从 [FFmpeg 官方网站](https://ffmpeg.org/download.html) 下载 FFmpeg。
2. 配置环境变量（自行查找具体步骤）。

## Telegram机器人
请自行查找具体步骤

## 使用说明

1. 在 resource 文件夹下放置录音文件。
2. 修改 `filename` 的值。
3. 运行程序即可得到识别结果。
