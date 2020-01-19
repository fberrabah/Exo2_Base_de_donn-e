from model.connectaccount import *
from controller.profil import *

class Verify():
    def __init__(self, p, pseudo, pwd, password):
        self.p = p
        self.pseudo = pseudo
        self.pwd = pwd
        self.password = password
        self.pseudo_ok = None
        self.password_ok = None 
        
    def check_pseudo(self, p, pseudo, pseudo_ok):
        """method for verify i pseudo entry is in
        bdd in champ pseudo"""
        for row in self.p:
            for i in row:
                if self.pseudo == i:
                    self.pseudo_ok = True
                    
   
   
    def check_password(self, pwd, password, password_ok):
        """method for verify password"""

        for row in self.pwd:
            for i in row:
                if self.password == i:
                    self.password_ok = True
                    self.password_ok


    def check_password_pseudo(self):
        
        if self.pseudo_ok == True and self.password_ok == True:
            space = Profil(self.pseudo)
            space.view_profil()
        else :
            print("Erreur sur le pseudo ou le mot de passe")
            return
