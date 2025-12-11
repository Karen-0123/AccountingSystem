from database.crud import insert_transaction

def add_transaction(user_id, data):
    category_id = data["category_id"]
    amount = data["amount"]
    txn_type = data["type"]
    memo = data.get("memo", "")
    
    result = insert_transaction(
        user_id,
        data["category_id"],
        data["amount"],
        data["type"],
        data["memo"]
    )

    if result["status"]:
        return {"msg": f"新增成功：{data['category_name']} {data['amount']}"}
    else:
        return {"msg": "新增失敗，請稍後再試"}
