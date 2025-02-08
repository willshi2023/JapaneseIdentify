import time
import traceback

from pydub import AudioSegment
from telegram import Update
from telegram.ext import Application, filters, ContextTypes
from telegram.ext import MessageHandler, CallbackContext

import language
import my_file
import my_message
import secret


# 将m4a音频转换成wav
def transfer_format(file_path):
    start = time.perf_counter()

    if file_path.endswith('.m4a'):
        # 转换m4a为wav
        sound = AudioSegment.from_file(file_path, format="m4a")
        file_path = file_path + '.wav'
        sound.export(file_path, format="wav")
    elif file_path.endswith('.ogg'):
        # 转换为wav格式（SpeechRecognition需要wav格式）
        sound = AudioSegment.from_ogg(file_path)
        file_path = file_path + '.wav'
        sound.export(file_path, format="wav")

    end = time.perf_counter()
    log_message = '录音文件格式转换耗费的时间：{:.2f}秒'.format(end - start)
    print(log_message)
    return log_message,file_path

# 处理上传的录音文件
async def handle_audio(update, context):
    audio = update.message.audio
    if audio:
        file = await context.bot.get_file(audio.file_id)
        filename,file_path1 = my_file.get_filename('m4a')
        await file.download_to_drive(file_path1)
        await transfer_text_and_send(file_path1)

# 处理语音消息
# 处理语音消息
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice
    if voice:
        # 下载语音文件
        file = await context.bot.get_file(voice.file_id)
        filename, file_path1 = my_file.get_filename('ogg')
        await file.download_to_drive(file_path1)
        await transfer_text_and_send(file_path1)


async def transfer_text_and_send(file_path1):
    file_path2 = ''
    try:
        # 将音频进行转换
        transfer_format_log_message, file_path2 = transfer_format(file_path1)
        # 将语音转换成文字
        transfer_text_log_message, text = language.transfer_text(file_path2)
        # 删除之前的文件
        my_file.delete_safe(file_path1)
        my_file.delete_safe(file_path2)
        # 发送消息到telegram
        message2 = (
            f'{transfer_text_log_message}\n'
            f'语音识别结果如下:\n'
        )
        my_message.send_message2group(message2)
        message2 = (
            f'*{text}*\n'
        )
        my_message.send_message2group(message2)
    except Exception as e:
        print("发生异常：", str(e))
        traceback.print_exc()
        try:
            message2 = (
                f'识别失败，请尝试其他音频\n'
            )
            my_message.send_message2group(message2)
            # 删除之前的文件
            my_file.delete_safe(file_path1)
            my_file.delete_safe(file_path2)
        except:
            pass


def main():
    application = Application.builder().token(secret.TELEGRAM_TOKEN).build()

    application.add_handler(MessageHandler(filters.AUDIO, handle_audio))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))

    application.run_polling()


if __name__ == '__main__':
    main()
