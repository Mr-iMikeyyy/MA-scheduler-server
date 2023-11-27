from db import DB
class Mechs():
    def __init__(self, db: DB) -> None:
        self.results = db.queryDB("SELECT * from mechanics")
        # print(self.mechs)