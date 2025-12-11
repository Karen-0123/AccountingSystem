# 用來測試 API 的程式（手動或自動測試）
# 用來模擬呼叫 Line Bot 或後端路由
from services.transaction_service import add_transaction

data = {
    "category_id": 1,
    "amount": 120,
    "type": "expense",
    "memo": "beef"
}

print(add_transaction("U123456", data))