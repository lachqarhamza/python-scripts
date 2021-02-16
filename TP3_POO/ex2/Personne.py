class Personne:
    def __init__(self, __nom, __sexe, __adresses):
        self.__nom = __nom
        self.__sexe = __sexe
        self.__adresses = __adresses
    
    @property
    def nom(self):
        return self.__nom

    @property
    def sexe(self):
        return self.__sexe

    @property
    def adresses(self):
        return self.__adresses

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @sexe.setter
    def sexe(self, value):
        self.__sexe = value

    @adresses.setter
    def adresses(self, value):
        self.__adresses = value
