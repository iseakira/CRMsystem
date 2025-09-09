import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = 'sample.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

##query = "INSERT INTO items(item_name, item_price) VALUES('おにぎり',100)"
query = "INSERT INTO items(item_name, item_price) VALUES('焼きおにぎり',120)"
##query = "INSERT INTO items(item_name) VALUES('酒おにぎり')"

cur.execute(query)
conn.commit()
conn.close()