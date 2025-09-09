from sqlalchemy.sql import insert
from models import engine, customers
import sqlalchemy

value1 = {"customer_id":'C002',
          "customer_name":'佐藤A子',
          "age":64,
          "gender":'女',
          }

query = customers.insert().values(value1)

conn = engine.connect()

try:
  result=conn.execute(query)
  if result.is_insert:
    print("insert成功")
    print("inserted_primary_key:", str(result.inserted_primary_key)[0])
  
except sqlalchemy.exc.IntegrityError :
  print("主キーの重複エラー")
conn.close()