from database.db import get_connection

def get_category_id_by_name(category_name: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT id
        FROM categories
        WHERE name = %s
    """
    cursor.execute(sql, category_name)
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return row["id"]
    return None
