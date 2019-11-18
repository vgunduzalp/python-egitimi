import psycopg2

connection = psycopg2.connect(user="postgres", password= "veysel",host="127.0.0.1",port="5432",database="pythonegitimi")


cursor = connection.cursor()
"""
cursor.execute("select version();")

a = cursor.fetchone()

"""

sql = """ insert into "Test" ("Ad","Soyad") values (%s,%s) """
"""
cursor.execute(sql,("ali","demir",))

connection.commit()
"""

sql = """ select * from "Test" """

cursor.execute(sql)
list = cursor.fetchall()

for i in list:
    print(i)





