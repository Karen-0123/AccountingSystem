# Flask 入口（Webhook、API 註冊）
from database.crud import add_user

# LINE會push資料到你的伺服器，https://你的伺服器/webhook
@app.route("/webhook", methods=["POST"]) 
def webhook():
    body = request.get_json()

    user_id = body["events"][0]["source"]["userId"]
    display_name = line_bot_api.get_profile(user_id).display_name

    add_user(user_id, display_name)

    return "ok"
