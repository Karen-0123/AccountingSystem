# app.py - Flask 入口（Webhook、API 註冊）

from flask import Flask, request, abort
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 匯入您在 my_linebot/line_bot_api.py 中定義的 line_bot_api 和 handler
from my_linebot.line_bot_api import line_bot_api, handler 

# 匯入專案的其他模組
from database.crud import add_user 
# from linebot.parser import parse_user_input # 假設您有這個檔案

# --- 1. 初始化 Flask 應用程式 ---
app = Flask(__name__)

# --- 2. LINE Webhook 處理路由 ---

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data(as_text=True)

    try:
        # 使用匯入的 handler 處理請求
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.error("Invalid signature. Check your channel access token/secret.")
        abort(400)

    return "OK"

# --- 3. 訊息事件處理器 (核心邏輯) ---

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    text = event.message.text
    
    # 執行您的資料庫邏輯
    try:
        profile = line_bot_api.get_profile(user_id)
        display_name = profile.display_name
        add_user(user_id, display_name) 
    except Exception as e:
        app.logger.error(f"Error handling user profile: {e}")
        
    # 回覆用戶訊息
    reply_text = f"收到您的訊息：{text}，已記錄用戶 ID: {user_id}"
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

# --- 4. 啟動伺服器 ---

if __name__ == "__main__":
    # 使用 Port 5000，或從環境變數讀取
    app.run(host="0.0.0.0", port=5000)