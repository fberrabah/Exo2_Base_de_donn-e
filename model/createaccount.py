from model.connection import *
import hashlib

class Createaccount():

    def __init__(self):
        self.choice = connection()
        self.name = None
        self.firstname = None
        self.pseudo = None
        self.email = None
        self.age = None
        self.password = None

        

    def create(self):
        self.choice.initialize_connection()
        self.name = input("Entrer votre nom :").lower()
        self.firstname = input("Entrer votre prénom :").lower()
        self.pseudo = input("Entrer votre pseudo :").lower()
        self.email = input("Entrer votre email :").lower()
        self.age = input("Entrer votre age :").lower()
        self.password = input("Entrer votre mot de passe :").lower()
        self.password = hashlib.sha1(self.password.encode()).hexdigest()
        self.choice.cursor.execute("INSERT INTO users(name, firstname, pseudo, email, age, password) VALUES"
                                  "(%s, %s, %s, %s, %s, %s )" ,(self.name, self.firstname, self.pseudo,self.email, self.age, self.password))
        self.choice.connection.commit()
        self.choice.close_connection()

