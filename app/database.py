import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(
            "hashguard.db"
        )


    def create(self):

        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports(
        id INTEGER PRIMARY KEY,
        score INTEGER
        )
        """)

        self.connection.commit()
