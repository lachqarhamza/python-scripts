class Voiture:
    def __init__(self):
        self.lumiere = 0
        self.vitesse = 0

    def setLumOn(self):
        self.lumiere = 1

    def setLumOff(self):
        self.lumiere = 0

    def setVitesse(self, vitesse):
        self.vitesse = vitesse

    def affichage(self):
        print("vitesse: ", self.vitesse)
        print("lumiere: ", self.lumiere)
