import sqlite3
from scrapeCongress import Scraper

class Database:
    def __init__(self):
        self.connection : sqlite3.Connection = None
        self.cursor : sqlite3.Cursor = None

    def connect(self):
        if self.connection:
            raise Exception("Connection Already Established")
        else:
            self.connection = sqlite3.connect('congress.db')

    def createCursor(self):
        if self.cursor:
            raise Exception("Cursor Already Created")
        else:
            self.cursor = self.connection.cursor()

    def deleteCursor(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        else:
            raise Exception("No Active Cursors")

    def deleteTable(self, name="Person"):
        if self.cursor:
            query = "DROP TABLE IF EXISTS '{Name}';".format(Name=name)
            self.execute(query)
        else:
            raise Exception("No Active Cursors")

    def close(self):
        if self.connection:
            if self.cursor:
                self.deleteCursor()
                self.cursor = None
            self.connection.close()
            self.connection = None
        else:
            raise Exception("No Active Connection")

    def retrieve(self, query):
        data = self.cursor.execute(query).fetchall()
        print(data)
        self.connection.commit()
        return data
    
    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()
    
    def refreshDatabase(self):
        scraper = Scraper()
        df = scraper.refreshDB()
        self.connect()
        self.createCursor()
        self.deleteTable("Person")
        df.to_sql('Person', self.connection, index=False)
        self.close()

    def getFirst(self, num = 1, name = "", party = "", state = "", office = ""):
        name, party, state, office = (str(name).lower() if name else None,
            str(party).lower() if party else None,
            str(state).lower() if state else None,
            str(office).lower() if office else None
        )
        sqlStrList = []
        sqlStrList = sqlStrList + ["Name like lower('%{name}%')".format(name=name)] if name else sqlStrList
        sqlStrList = sqlStrList + ["Party like lower('%{party}%')".format(party=party)] if party else sqlStrList
        sqlStrList = sqlStrList + ["State like lower('%{state}%')".format(state=state)] if state else sqlStrList
        sqlStrList = sqlStrList + ["Branch like lower('%{office}%')".format(office=office)] if office else sqlStrList
        query = "SELECT * FROM Person "

        if len(sqlStrList):
            query += "WHERE "
        query += " AND ".join(sqlStrList)
        query += " LIMIT {num}".format(num=num)
        try:
            self.connect()
            self.createCursor()
            results = self.retrieve(query)
            self.connection.commit()
            return results
        except:
            pass
        finally:
            self.deleteCursor()
            self.close()

    def getAll(self, name = "", party = "", state = "", office = ""):
        name, party, state, office = (str(name).lower() if name else None,
            str(party).lower() if party else None,
            str(state).lower() if state else None,
            str(office).lower() if office else None
        )
        sqlStrList = []
        sqlStrList = sqlStrList + ["Name like lower('%{name}%')".format(name=name)] if name else sqlStrList
        sqlStrList = sqlStrList + ["Party like lower('%{party}%')".format(party=party)] if party else sqlStrList
        sqlStrList = sqlStrList + ["State like lower('%{state}%')".format(state=state)] if state else sqlStrList
        sqlStrList = sqlStrList + ["Branch like lower('%{office}%')".format(office=office)] if office else sqlStrList
        query = "SELECT * FROM Person "
        if len(sqlStrList):
            query += "WHERE "
        query += " AND ".join(sqlStrList)
        try:
            self.connect()
            self.createCursor()
            results = self.retrieve(query)
            self.connection.commit()
            return results
        except:
            pass
        finally:
            self.deleteCursor()
            self.close()