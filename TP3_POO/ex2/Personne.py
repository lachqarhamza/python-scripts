class Personne:
    def __init__(self, __nom, __sexe, __adresses):
        self.__nom = __nom
        self.__sexe = __sexe
        self.adresse = __adresses
    
    @property
    def __nom(self):
        return self.___nom

    @property
    def __sexe(self):
        return self.___sexe

    @property
    def __adresses(self):
        return self.___adresses

    @__nom.setter
    def __nom(self, value):
        self.___nom = value

    @__sexe.setter
    def __sexe(self, value):
        self.___sexe = value

    @__adresses.setter
    def __adresses(self, value):
        self.___adresses = value
