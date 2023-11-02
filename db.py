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
        self.cursor = self.conn.cursor()
        
    
    def queryDB(self, query: str):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results
