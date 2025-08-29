import cx_Oracle

class DAOObalky:
    connection = None
    cursor = None

    def __init__(self):
        from config_db import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_SID
        dsn = cx_Oracle.makedsn(DB_HOST, DB_PORT, sid=DB_SID)
        self.connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, dsn)
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
        


# Spouštěcí blok mimo třídu
if __name__ == "__main__":
    try:
        dao = DAOObalky()
        print("Spojení s databází bylo úspěšné.")
        dao.close()
    except Exception as e:
        print("Chyba při spojení s databází:", e)
