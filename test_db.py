from db import get_connection
try:
    conn = get_connection()
    print("DB conncetion successfully..!!")
    conn.close()
except Exception as e:
    print(f"DB Connection failed: {e}")