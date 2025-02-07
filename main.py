import os
import time

from pydub import AudioSegment
from telegram.ext import Application, MessageHandler, filters

import language
import my_file
import my_message
import secret


# 将m4a音频转换成wav
def transfer_format(file_path):
    start = time.perf_counter()
    # 转换m4a为wav
    sound = AudioSegment.from_file(file_path, format="m4a")
    file_path = file_path + '.wav'
    sound.export(file_path, format="wav")
    end = time.perf_counter()
    log_message = '录音文件格式转换耗费的时间：{:.2f}秒'.format(end - start)
    print(log_message)
    return log_message,file_path

async def handle_audio(update, context):
    audio = update.message.audio
    if audio:
        file = await context.bot.get_file(audio.file_id)
        filename,file_path1 = my_file.get_filename()
        await file.download_to_drive(file_path1)
        # 将音频进行转换
        transfer_format_log_message,file_path2 =  transfer_format(file_path1)
        # 将语音转换成文字
        transfer_text_log_message,text = language.transfer_text(file_path2)
        # 删除之前的文件
        my_file.delete_safe(file_path1)
        my_file.delete_safe(file_path2)
        # 发送消息到telegram
        message2 = (
            f' *{transfer_text_log_message}*\n'
            f'语音识别结果: *{text}*\n'
        )
        my_message.send_message2group(message2)


def main():
    application = Application.builder().token(secret.TELEGRAM_TOKEN).build()

    application.add_handler(MessageHandler(filters.AUDIO, handle_audio))

    application.run_polling()


if __name__ == '__main__':
    main()
