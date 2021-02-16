class Adresse:
    def __init__(self, __rue, __ville, __code_postal):
        self.__rue = __rue
        self.__ville = __ville
        self.__code_postal = __code_postal

    @property
    def rue(self):
        return self.__rue

    @property
    def ville(self):
        return self.__ville

    @property
    def code_postal(self):
        return self.__code_postal

    @rue.setter
    def rue(self, value):
        self.__rue = value

    @ville.setter
    def ville(self, value):
        self.__ville = value

    @code_postal.setter
    def code_postal(self, value):
        self.__code_postal = value
