import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = 'sample.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "UPDATE items SET item_price = 150 WHERE item_id=2"
##query = "INSERT INTO items(item_id, item_name, item_price) VALUES(1,'おにぎり',100)"

cur.execute(query)
conn.commit() 
conn.close()