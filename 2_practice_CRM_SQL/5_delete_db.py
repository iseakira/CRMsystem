import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = 'CRM.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "DELETE FROM purchases WHERE purchase_id=1"


cur.execute(query)
conn.commit() 
conn.close()