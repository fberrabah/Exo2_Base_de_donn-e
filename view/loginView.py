from model.connection import * 

class Longinview():
    def __init__(self):
        self.choice = connection()
    
    def read(self):
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM users;")
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        return test


