# 新增 / 查詢 / 更新 / 刪除
# 每次操作後須確實關閉連線
from database.db import get_connection
from datetime import datetime

# 新增LINE BOT的json資料到資料庫
def insert_transaction(user_id, category_id, amount, type, memo):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        query = """
            INSERT INTO transactions 
            (user_id, category_id, amount, type, timestamp, memo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (user_id, category_id, amount, type, time_now, memo))
        conn.commit()

        new_id = cursor.lastrowid

        return {
            "status": "success",
            "id": new_id
        }
        
    except Exception as e:
        print("SQL 執行錯誤：", repr(e))   # ✅ 這一行會顯示真正錯誤原因
        return {"status": "error", "msg": str(e)}
    
    finally:
        cursor.close()
        conn.close()


# # 查詢
# def get_transactions_by_date(user_id, date):
#     # date 格式: "2025-12-07"
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#         SELECT category, amount, type, timestamp, memo
#         FROM transactions
#         WHERE user_id = %s AND timestamp LIKE %s
#         ORDER BY timestamp ASC
#     """

#     cursor.execute(query, (user_id, f"{date}%"))
#     rows = cursor.fetchall()
    
#     conn.close()

#     result = []
#     for row in rows:
#         result.append({
#             "category": row[0],
#             "amount": row[1],
#             "type": row[2],
#             "timestamp": row[3],
#             "memo": row[4]
#         })

#     return {
#         "transactions": result
#     }

# # 刪除
# def delete_transaction(transaction_id):
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = "DELETE FROM transactions WHERE id = %s"
#     cursor.execute(query, (transaction_id,))
#     conn.commit()

#     affected = cursor.rowcount  # 1 = 有刪到；0 = ID 不存在
#     conn.close()

#     return {
#         "status": "success" if affected > 0 else "not_found",
#         "deleted_rows": affected
#     }


# def add_user(line_user_id, display_name=None):
#     conn = get_connection()
#     cursor = conn.cursor()

#     sql = "INSERT INTO users (line_user_id, display_name) VALUES (%s, %s)"
#     cursor.execute(sql, (line_user_id, display_name))
    
#     conn.commit()
#     cursor.close()
#     conn.close()
