from Db import Db

db = Db()

#sql = """ delete from "Test" where "Id"=2 """

#db.execute(sql)

sql = """ select * from "Test" where "Id"<%s or "Id">%s """

data = db.read_data(sql,(5,1))

for i in data:
    print(i)





