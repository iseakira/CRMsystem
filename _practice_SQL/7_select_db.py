import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = 'sample.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "SELECT item_id, item_name, item_price FROM items"

cur.execute(query)
print(cur.fetchmany(2))
conn.commit()
conn.close()