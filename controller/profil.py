import sys
from controller.delete import *
from controller.change import *   
class Profil():

    def __init__(self, pseudo):
        self.pseudo = pseudo

    def view_profil(self):
        profilchoice = ""
        surchoice = ""
        print("\n---------------------------\n")
        print("Bienvenue sur votre profil")
        print("\n---------------------------\n")
        while profilchoice != "q":
            profilchoice= input('(a) pour changer \n(b) pour supprimer \n(q) pour quitter :')
            if profilchoice == "q":
                print("A bientôt.")
                sys.exit() 

            if profilchoice == "b":
                surchoice=input("Attention si vous validez votre compte sera supprimé et vous quitterez l'application\n (o) pour supprimer\n (n) pour revenir au menu :")
                if surchoice == "o":
                    user_choice = Delete(self.pseudo)
                    user_choice.del_account()
                    print("Compte supprimé.\nA bientôt.")
                    sys.exit() 
                if surchoice == "n":       
                    az = view_profil()
                    az.view_profil

            if profilchoice == "a": 
                user_choice = Change(self.pseudo)
                user_choice.change_datta()
                print("Compte modifié")

        
