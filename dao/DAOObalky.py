import cx_Oracle

class DAOObalky:
    connection = None
    cursor = None

    def __init__(self, user, password):
        # DSN pro ORADB.JCU.CZ:1526/JIS2
        dsn = cx_Oracle.makedsn("oradb.jcu.cz", 1526, sid="JIS2")
        self.connection = cx_Oracle.connect(user, password, dsn)
        self.cursor = self.connection.cursor()
    
    def getObalky(self):
        # Vrací pole objektů třídy Karta (zatím prázdné)
        from core.karta import Karta
        return []

    def get_all(self):
        self.cursor.execute("SELECT * FROM OBALKY")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
        

    if __name__ == "__main__":
        from config_db import DB_USER, DB_PASSWORD
        try:
            dao = DAOObalky(DB_USER, DB_PASSWORD)
            print("Spojení s databází bylo úspěšné.")
            dao.close()
        except Exception as e:
            print("Chyba při spojení s databází:", e)
