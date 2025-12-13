# 解析文字變成data

def parse_transaction_message(text: str):
    parts = text.strip().split()

    if len(parts) < 4 or parts[0] != "記帳":
        return None, "格式錯誤，請使用：記帳 類別 金額 備註"

    _, category_name, amount_str, *memo_parts = parts

    if not amount_str.isdigit():
        return None, "金額必須是數字"

    data = {
        "category_name": category_name,
        "amount": int(amount_str),
        "type": "expense",
        "memo": " ".join(memo_parts)
    }

    return data, None
