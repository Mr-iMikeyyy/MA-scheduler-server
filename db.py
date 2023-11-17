import mysql.connector

class DB():
    
    def __init__(self) -> None:

        self.dbconfig = {
            'user' : 'root', 
            'password' : 'pw4MarksAutoSchedule',
            'host' : '127.0.0.1', 
            'database' : "marksauto"
        }

        self.conn = mysql.connector.connect(**self.dbconfig)
        
    
    def queryDB(self, query: str):
        cursor = self.conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    
    def insertDB(self, query: str, val: tuple):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, val)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("insert failed: \n")
            print(err)
        finally:
            print("affected rows = {}".format(cursor.rowcount))
            cursor.close()

