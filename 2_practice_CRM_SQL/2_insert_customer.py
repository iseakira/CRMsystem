import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = 'CRM.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()


value1 = ('C001','佐藤A子',64,'女')
value2 = ('C002','鈴木B子',34,'女')
value3 = ('C003','斎藤C男',21,'男')
query = "INSERT INTO customers(customer_id,customer_name,age,gender) VALUES(?,?,?,?)"


cur.execute(query,value3)
conn.commit()
conn.close()