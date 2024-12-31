import sqlite3

class FileHandler():
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()

    def create_table(self):

        with open("create_table.sql", "r") as query_file:
            query_script = query_file.read()

        self.cursor.executescript(query_script)
        self.connection.commit()
    
    def close(self):
        self.connection.close()


file_handler = FileHandler()
file_handler.create_table()
file_handler.close()