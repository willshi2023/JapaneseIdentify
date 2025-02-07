import requests

import constant
import secret

API_TOKEN = secret.TELEGRAM_TOKEN
CHAT_ID = None

def get_chat_id():
    global CHAT_ID

    if CHAT_ID:
        return CHAT_ID

    url = f"https://api.telegram.org/bot{API_TOKEN}/getUpdates"
    response = requests.get(url)
    data = response.json()

    if data["result"]:
        CHAT_ID = data["result"][0]["message"]["chat"]["id"]
        return CHAT_ID
    else:
        return None

# 获取更新的函数
def get_updates():
    url = f'https://api.telegram.org/bot{API_TOKEN}/getUpdates'
    response = requests.get(url)
    return response.json()



def send_message(message):
    print(message)
    chat_id = get_chat_id()
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message,"parse_mode": "Markdown"}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        # print("Message sent successfully!")
        pass
    else:
        print("Failed to send message.")


# 发送消息的函数
def send_message2group(text):
    try:
        url = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
        payload = {
            'chat_id': constant.CHAT_ID,
            'text': text,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, data=payload)
        return response.json()
    except:
        pass

if __name__ == '__main__':
    # print(get_updates())
    # CHAT_ID1 = get_chat_id()
    # print(CHAT_ID1)
    # 使用示例
    currency = 'OKB-USDT'
    transaction_type = '卖出'
    current_position_cost = 10000
    treat_amount = 10000
    current_price = 10000
    transaction_count = 3.65
    currency_count = 10000
    profit = 10000
    profit_rate100 = 10000
    total_profit_rate100 = 0.15
    message2 = (
        f'货币种类: *{currency}*\n'
        f'交易类型: *{transaction_type}*\n'
        f'本次建仓成本金额: *{current_position_cost}*\n'
        f'本次交易金额: *{treat_amount}*\n'
        f'当前币价: *{current_price}*\n'
        f'本次交易币数量: *{transaction_count}*\n'
        f'仓位剩余货币个数: *{currency_count}*\n'
        f'本次盈利: *{profit}*\n'
        f'本次盈利比例: *{profit_rate100}%*\n'
        f'累计盈利比例: *{total_profit_rate100}%*'
    )
    send_message2group(message2)
