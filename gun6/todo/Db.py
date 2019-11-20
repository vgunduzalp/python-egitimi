import psycopg2

class Db():

    def open(self):
        self.connection = psycopg2.connect(user="postgres",
                                           password= "veysel",
                                           host="127.0.0.1",
                                           port="5432",
                                           database="pythonegitimi")
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def execute(self,sql,params):
        self.open()
        self.cursor.execute(sql,params)
        self.connection.commit()
        self.close()

    def read_data(self,sql,params=()):
        self.open()
        self.cursor.execute(sql,params)
        result = self.cursor.fetchall()
        self.close()
        return result

    def read_first_data(self,sql,params=()):
        self.open()
        self.cursor.execute(sql,params)
        result = self.cursor.fetchone()
        self.close()
        return result