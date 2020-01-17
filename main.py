from model.connection import *
from model.connectaccount import *
from model.createaccount import *
from controller.verify import *
import sys


test=connection()
test.initialize_connection()
test.close_connection()


if __name__=='__main__':

    pseudo_ok = False
    password_ok = False
    choix=""     
    print("\n----------------------------------------\n")
    print('Bienvenue dans votre application préférée.')
    print("\n----------------------------------------\n")
    while choix != "q":
        choix = input("Avez_vous déjà un compte? \n\n(o) pour vous connecter : \n(n) si vous souhaitez créer un compte : \n(q) pour quitter : ").lower()
        if choix == "o":          
            log = Connectaccount()
            log.connect()

        if choix == "n":
            
            test= Createaccount()
            test.create()

        if choix == "q":
            print("A bientôt.")
            sys.exit() 
