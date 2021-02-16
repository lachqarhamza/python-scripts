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
            if p.nom == s:
                return p
        return None

    def exists_code_postal(self, cp):
        for p in self.personnes:
            for a in p.adresses:
                if a.code_postal == cp:
                    return True
        return False
