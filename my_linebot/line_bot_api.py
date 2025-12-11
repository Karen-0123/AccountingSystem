# c:\python\AccountingSystem\my_linebot\line_bot_api.py 或 __init__.py

import os
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler

load_dotenv() # 確保這行在最上面，用來載入 .env 內容

# 必須用 os.getenv() 從環境變數中獲取字串值
CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

# 檢查 (可選)
if not CHANNEL_ACCESS_TOKEN or not CHANNEL_SECRET:
    raise ValueError("LINE_CHANNEL_ACCESS_TOKEN 或 LINE_CHANNEL_SECRET 遺失。請檢查 .env 檔案。")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)