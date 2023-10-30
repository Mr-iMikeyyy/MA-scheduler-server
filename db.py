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
        
    
    def queryDB(self, type: str, query: str):
        cursor = self.conn.cursor()
        cursor.execute(query)
