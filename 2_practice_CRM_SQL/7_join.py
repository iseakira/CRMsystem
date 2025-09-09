import sqlite3
import os
import pandas as pd

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = 'CRM.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "SELECT * FROM purchases\
        JOIN purchases_details\
        ON purchases.purchase_id=purchases_details.purchase_id"
df = pd.read_sql_query(query, conn)
print(df)

conn.commit()
conn.close()