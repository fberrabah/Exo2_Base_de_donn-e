from model.connection import *
from getpass import *
from controller.verify import *
import hashlib

class Connectaccount():
    def __init__(self):
        self.log = connection()
        self.pseudo = None
        self.password = None
        self.p = None
        self.pwd = None
        self.pseudo_ok = None
        self.password_ok = None
        self.pseudo_password = False
        
        
    def connect(self):

        self.log.initialize_connection()
        self.pseudo = input("Entrer votre pseudo :").lower()
        self.password = getpass()
        self.password = hashlib.sha1(self.password.encode()).hexdigest()
        self.log.cursor.execute("SELECT pseudo FROM users;")
        self.p = self.log.cursor.fetchall()
        self.log.cursor.execute("SELECT password FROM users;")
        self.pwd = self.log.cursor.fetchall()
        a = Verify(self.p, self.pseudo, self.pwd, self.password)
        a.check_pseudo(self.p, self.pseudo, self.pseudo_ok)
        a.check_password(self.pwd, self.password, self.password_ok)
        a.check_password_pseudo()
