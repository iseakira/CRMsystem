import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = 'sample.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "ALTER TABLE items ADD quantity INTGER"
query = "ALTER TABLE items DROP quantity"     

cur.execute(query)
conn.commit()
conn.close()