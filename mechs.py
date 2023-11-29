from db import DB
class Mechs():
    def __init__(self, db: DB) -> None:
        results = db.queryDB("SELECT * from mechanics", "")

        self.mechs = {}

        for x in range(len(results)):
            self.mechs[results[x][0]] = results[x][1]

        print(self.mechs)

        