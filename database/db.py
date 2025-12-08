# 每次程式執行時取得資料庫連線
import pymysql
from pymysql.cursors import DictCursor

# 資料庫連線設定
DB_CONFIG = {
    "host": "localhost",     
    "user": "root",          
    "password": "",          
    "database": "accountingsystemdb",
    "charset": "utf8mb4",
    "cursorclass": DictCursor
}

# 每次請求(CRUD)都要建立新連線
# Linebot 傳一句話 → 進入 Flask → 做一次資料庫操作 → 關閉連線 → 回覆 Linebot
def get_connection():
    return pymysql.connect(**DB_CONFIG)
