# my_linebot/handler.py
from flask import Blueprint, request, abort
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from .line_bot_api import line_bot_api, handler
from .parser import parse_user_input
from database import crud

bp = Blueprint("my_linebot", __name__)

@bp.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    user_id = event.source.user_id
    text = event.message.text.strip()
    parsed = parse_user_input(text)
    if parsed["ok"]:
        rec = crud.create_record(
            user_id=user_id,
            amount=parsed["amount"],
            category=parsed["category"],
            note=parsed.get("note", "")
        )
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"已記錄：{parsed['category']} {parsed['amount']} 元")
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="無法解析輸入，輸入範例：午餐 150 或 /help")
        )
