from database.crud import insert_transaction#, get_transactions_by_date

# 1. 新增一筆資料
res = insert_transaction(
    user_id="U123456",
    category_id=1, # transactions 存「數字 ID」，categories 存「文字名稱」
    amount=120,
    type="expense",
    memo="beef"
)

print(res)

# # 2. 查詢今天資料
# data = get_transactions_by_date("U123456", "2025-12-07")
# print(data)

# 輸出
# {"status": "success", "id": 1}
# {
#   "transactions": [
#     {
#       "category": "餐飲",
#       "amount": 120,
#       "type": "expense",
#       "timestamp": "2025-12-07 21:05:10"
#     }
#   ]
# }
