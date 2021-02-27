from Voiture import Voiture

class Decapotable(Voiture):
    def __init__(self):
        self.eToit = 0
        super().__init__()

    def setToitHaut(self):
        self.eToit = 1

    def setToitBas(self):
        self.eToit = 0

    def affichage(self):
        super().affichage()
        print("etat du toit: ", self.eToit)
