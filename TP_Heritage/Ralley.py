from Voiture import Voiture

class Ralley(Voiture):
    def setVitesse(self, vitesse):
        if vitesse > 200:
            print("vitesse should be <= 200, here,  an exception should be raised")
        else:
            super().setVitesse(vitesse)
