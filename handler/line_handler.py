# 接收 LINE 傳來的 event（文字訊息）
# 呼叫 parser（parse_message）解析使用者輸入
# 呼叫 service.add_transaction()
# 把 service 回傳的字串回傳給 LINE

# 範例而已，程式需修改
# from linebot import LineBotApi, WebhookHandler
# from utils.parser import parse_message
# from services.transaction_service import add_transaction

# def handle_text_message(event):
#     user_id = event.source.user_id
#     text = event.message.text

#     data = parse_message(text)
#     result = add_transaction(user_id, data)

#     reply_message(event.reply_token, result["msg"])
