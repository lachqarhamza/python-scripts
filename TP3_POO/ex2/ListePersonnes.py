class ListePersonnes:
    def __init__(self, __personnes):
        self.__personnes = __personnes

    @property
    def personnes(self):
        return self.__personnes

    @personnes.setter
    def personnes(self, value):
        self.__personnes = value

    def find_by_nom(self, s):
        for p in self.personnes:
            for p in self.__personnes:
                if p.nom == s:
                    return p
        return None

    def exists_code_postal(self, cp):
        pass
        for p in self.__personnes:
            for a in p.__adresses:
                if a.__code_postal == cp:
                    return True
        return False

