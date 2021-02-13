class Adresse:
    def __init__(self, __rue, __ville, __code_postal):
        self.__rue = __rue
        self.__ville = __ville
        self.__code_postal = __code_postal

    @property
    def __rue(self):
        return self.___rue

    @property
    def __ville(self):
        return self.___ville

    @property
    def __code_postal(self):
        return self.___code_postal

    @__rue.setter
    def __rue(self, value):
        self.___rue = value

    @__ville.setter
    def __ville(self, value):
        self.___ville = value

    @__code_postal.setter
    def __code_postal(self, value):
        self.___code_postal = value

