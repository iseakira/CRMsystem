from sqlalchemy.sql import insert
from models import engine, items
import sqlalchemy



value1 = ( {"item_id":"S001",
          "item_name": "お茶",
          "price":150,
          },
          {"item_id":"S002",
          "item_name": "おにぎり",
          "price":100,
                  },
          )


query = items.insert().values(value1)

conn = engine.connect()

try:
  result=conn.execute(query)
  if result.is_insert:
    print("insert成功")
    print("inserted_primary_key:", str(result.inserted_primary_key)[0])
  
except sqlalchemy.exc.IntegrityError :
  print("主キーの重複エラー")
conn.close()