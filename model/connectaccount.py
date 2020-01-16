from model.connection import *
from getpass import *

class Connectaccount():
    def __init__(self):
        self.log = connection()
        self.pseudo = None
        self.password = None 
        
    def connect(self):
        self.log.initialize_connection()
        self.pseudo = input("Entrer votre pseudo :").lower()
        #verif=Connectaccount()
        #verif.check_pseudo()

        self.password = getpass()

    def check_pseudo(self):
        self.log.cursor.execute("SELECT pseudo FROM users;")
        p=self.log.cursor.fetchall()
        self.log.cursor.check_pseudo(self.pseudo, p)
        if self.pseudo in p:
            print("yes")
        else:
            print("no")